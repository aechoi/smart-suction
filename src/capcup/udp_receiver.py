import argparse
from collections import deque
import time
import socket
import struct

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

# UDP Setup
# UDP_IP = "192.168.1.50"
UDP_IP = "192.168.10.50"
# UDP_PORT = 50001
UDP_PORT = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", UDP_PORT))

print("Listening...")

raw, addr = sock.recvfrom(1024)

# Must match struct layout from ESP32
timestamp, *values = struct.unpack("<Q8l", raw)
# data_points = 8 + 1  # 8 channels + 1 actuation flag
data_points = len(values)

# Plotting Setup ##########

window = 100
data = deque([values] * window, maxlen=window)
offsets = np.array(values) - 10000 * np.arange(data_points)
offsets = np.zeros_like(values)
if viz:
    plt.ion()
    fig, ax = plt.subplots()
    channels = ax.plot(np.array(data) - offsets)
    # ax.legend(
    #     [f"C{i+1}" for i in range(data_points - 1)] + ["Actuation"], loc="upper left"
    # )
    ax.legend([f"C{i+1}" for i in range(data_points)], loc="upper left")
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
                theta1=idx * 45 + 90 + 2,
                theta2=idx * 45 + 45 + 90 - 2,
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

last_actuation = time.time()
last_val = None
with open(file, "w") as f:
    while True:
        # if (time_stop != 0) and (time.time() - last_actuation > time_stop):
        #     print(f"Last actuation longer than {time_stop} seconds ago. Stopping.")
        #     break

        raw, addr = sock.recvfrom(1024)
        timestamp, *values = struct.unpack("<Q8l", raw)
        if len(values) != data_points:
            raise ValueError(
                f"Expected {data_points} values, got {len(values)}. {values}"
            )
        if values[-1] == 1:
            last_actuation = time.time()
        data.append(values)
        f.write(str(timestamp) + " " + str(values) + "\n")
        f.flush()

        if zeros is None:
            zeros = np.array(values)
        norm_caps = np.array(values) - zeros

        if last_val is None:
            last_val = norm_caps

        if viz:
            for idx, (ch, datum, offset) in enumerate(
                zip(channels, zip(*data), offsets)
            ):
                # scale = 10000 if idx == data_points - 1 else 1
                scale = 1
                ch.set_ydata(np.array(datum) * scale - offset)
                ch.set_xdata(range(len(datum)))
            ax.relim()
            ax.autoscale_view()
            plt.pause(0.01)
        if viz2:
            scale = 100000
            alpha = 0.01
            lp_val = last_val * (1 - alpha) + norm_caps * alpha

            colors = cmap(norm((norm_caps) / scale))[::-1]
            for arc, color in zip(arcs, colors):
                arc.set_color(color)
            fig2.canvas.draw_idle()
            plt.pause(0.01)
