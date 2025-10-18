import argparse
from collections import deque
import serial
import time

import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from matplotlib.widgets import Button
import numpy as np

# Parse args
parser = argparse.ArgumentParser()
parser.add_argument(
    "-f", "--file", type=str, default="test", help="File name to save data to"
)
parser.add_argument(
    "-t",
    "--time_stop",
    type=int,
    default=0,
    help="Time from last actuation to stop recording",
)
parser.add_argument(
    "--no-viz",
    action="store_false",
    dest="viz",
    help="Turn off the visualizer",
)
parser.add_argument(
    "--no-viz2",
    action="store_false",
    dest="viz2",
    help="Turn off the second vizualizer",
)
args = parser.parse_args()

file = args.file + ".csv"
time_stop = args.time_stop
viz = args.viz
viz2 = args.viz2

print("Saving to", file)

# Serial Setup
data_points = 8 + 1  # 8 channels + 1 actuation flag
ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)
print("Attempting to read...")
# Get first entry to initialize plot
while True:
    try:
        line = ser.readline().decode("utf-8").strip()
        values = [int(entry) for entry in line.split(" ")]
        if len(values) == data_points:
            break
    except Exception as e:
        pass
print("Stream read, starting")

# Plotting Setup ##########

window = 100
data = deque([values] * window, maxlen=window)
offsets = np.array(values) - 10000 * np.arange(data_points)
if viz:
    plt.ion()
    fig, ax = plt.subplots()
    channels = ax.plot(np.array(data) - offsets)
    ax.legend(
        [f"C{i+1}" for i in range(data_points - 1)] + ["Actuation"], loc="upper left"
    )
    ax.set_xlabel("Samples")
    ax.set_ylabel("Normalized and Offset ADC Counts")
    ax.set_title("Live Viewer")

zeros = None
scale = 100000
if viz2:
    plt.ion()
    fig2, ax2 = plt.subplots()
    ax2.axis("off")
    arcs = []

    text_r = 0.75
    text_thetas = np.linspace(
        np.pi / 8 + np.pi / 2, 2 * np.pi - np.pi / 8 + np.pi / 2, 8
    )
    text_x = text_r * np.cos(text_thetas)
    text_y = text_r * np.sin(text_thetas)
    for idx in range(8):
        arcs.append(
            Arc(
                (0, 0),
                1,
                1,
                angle=0,
                theta1=idx * 45 + 90,
                theta2=idx * 45 + 45 + 90,
                lw=15,
            )
        )
        ax2.text(text_x[-1 - idx], text_y[-1 - idx], f"{idx + 1}")
        ax2.add_patch(arcs[-1])

    ax2.set_xlim(-1, 1)
    ax2.set_ylim(-1, 1)
    ax2.set_aspect("equal")
    cmap = plt.cm.seismic
    norm = plt.Normalize(vmin=-1, vmax=1)

    # Define the callback function
    def on_button_click(event):
        global zeros
        zeros = None

    # Create a button axis (position: [left, bottom, width, height])
    button_ax = plt.axes([0.4, 0.05, 0.2, 0.075])
    button = Button(button_ax, "Reset Zero")

    # Connect the callback
    button.on_clicked(on_button_click)

############################


class BufferMonitor:
    def __init__(self, ser, max_buffer=4096):
        self.ser = ser
        self.max_buffer = max_buffer
        self.overflow_count = 0

    def safe_read(self, size):
        """Read with buffer overflow protection"""
        waiting = self.ser.in_waiting

        if waiting > self.max_buffer:
            print(f"!!!  Buffer overflow: {waiting} bytes")
            # Clear excess data
            excess = waiting - self.max_buffer
            discarded = self.ser.read(excess)
            self.overflow_count += 1
            print(f"Discarded {len(discarded)} bytes")

        return self.ser.read(min(size, waiting))

    def get_stats(self):
        return {
            "waiting": self.ser.in_waiting,
            "buffer_usage": f"{self.ser.in_waiting}/{self.max_buffer}",
            "overflows": self.overflow_count,
        }


class BufferOverflowError(IOError):
    pass


monitor = BufferMonitor(ser)
buffer = ""
last_actuation = time.time()
with open(file, "w") as f:
    while True:
        if (time_stop != 0) and (time.time() - last_actuation > time_stop):
            print(f"Last actuation longer than {time_stop} seconds ago. Stopping.")
            break
        chunk = monitor.safe_read(ser.in_waiting or 1).decode()
        if not chunk:
            continue
        buffer += chunk

        while "\n" in buffer:
            stats = monitor.get_stats()
            if stats["overflows"] > monitor.max_buffer:
                raise BufferOverflowError(
                    "!!! Buffer Overflows Detected !!! Lower sample rate or increase baud"
                )
            if viz:
                ax.set_title(
                    f"Live Viewer | Buffer: {stats['buffer_usage']} | Overflows: {stats['overflows']}"
                )
            line, buffer = buffer.split("\n", 1)
            print("Buffer:", stats["buffer_usage"], "| Data:", line)
            line = line.strip()
            if not line:
                continue

            try:
                values = [int(entry) for entry in line.split(" ")]
                if len(values) != data_points:
                    raise ValueError(
                        f"Expected {data_points} values, got {len(values)}. {values}"
                    )
                if values[-1] == 1:
                    last_actuation = time.time()
                data.append(values)

                f.write(str(time.time()) + " " + line + "\n")
                f.flush()

                if viz:
                    for idx, (ch, datum, offset) in enumerate(
                        zip(channels, zip(*data), offsets)
                    ):
                        scale = 10000 if idx == data_points - 1 else 1
                        ch.set_ydata(np.array(datum) * scale - offset)
                        ch.set_xdata(range(len(datum)))
                    ax.relim()
                    ax.autoscale_view()
                    plt.pause(0.01)
                if viz2:
                    if zeros is None:
                        zeros = np.array(values[:-1])
                    colors = cmap(norm((values[:-1] - zeros) / scale))[::-1]
                    for arc, color in zip(arcs, colors):
                        arc.set_color(color)
                    fig2.canvas.draw_idle()
                    plt.pause(0.01)

            except Exception as e:
                print(f"Error processing line: {e}")
