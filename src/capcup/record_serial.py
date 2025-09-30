import serial
import matplotlib.pyplot as plt
from collections import deque
import time
import numpy as np

file = "test.csv"
file = "250929_1503_50mm_ring_centerG_ringT.csv"
data_points = 8
window = 100

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
while True:
    try:
        line = ser.readline().decode("utf-8").strip()
        values = [int(entry) for entry in line.split(" ")]
        if len(values) == data_points:
            break
    except Exception as e:
        pass

data = deque([values] * window, maxlen=window)
offsets = np.array(values) - 10000 * np.arange(data_points)

plt.ion()
fig, ax = plt.subplots()
lines = ax.plot(np.array(data) - offsets)
ax.legend([f"Ch {i+1}" for i in range(data_points)], loc="upper left")
ax.set_xlabel("Samples")
ax.set_ylabel("Normalized and Offset ADC Counts")
ax.set_title("Live Viewer")

with open(file, "w") as f:
    while True:
        try:
            line = ser.readline().decode("utf-8").strip()
            print(line)
            if not line:
                continue

            f.write(str(time.time()) + " " + line + "\n")
            f.flush()

            values = [int(entry) for entry in line.split(" ")]
            if len(values) != data_points:
                continue
            data.append(values)
            for line, datum, offset in zip(lines, zip(*data), offsets):
                line.set_ydata(np.array(datum) - offset)
                line.set_xdata(range(len(datum)))
            ax.relim()
            ax.autoscale_view()
            plt.pause(0.01)
        except Exception as e:
            print(f"Error: {e}")
