import argparse
from collections import deque
import serial
import time

import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument(
    "-f", "--file", type=str, default="test", help="File name to save data to"
)
args = parser.parse_args()

file = args.file + ".csv"
print("Saving to", file)
data_points = 8 + 1
window = 100

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
print("Attempting to read...")
while True:
    try:
        line = ser.readline().decode("utf-8").strip()
        values = [int(entry) for entry in line.split(" ")]
        if len(values) == data_points:
            break
    except Exception as e:
        pass
print("Stream read, starting")

data = deque([values] * window, maxlen=window)
offsets = np.array(values) - 10000 * np.arange(data_points)

plt.ion()
fig, ax = plt.subplots()
channels = ax.plot(np.array(data) - offsets)
ax.legend([f"C{i+1}" for i in range(data_points - 1)] + ["Actuation"], loc="upper left")
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
            for idx, (ch, datum, offset) in enumerate(
                zip(channels, zip(*data), offsets)
            ):
                scale = 10000 if idx == data_points - 1 else 1
                ch.set_ydata(np.array(datum) * scale - offset)
                ch.set_xdata(range(len(datum)))
            ax.relim()
            ax.autoscale_view()
            plt.pause(0.01)
        except Exception as e:
            print(f"Error: {e}")
