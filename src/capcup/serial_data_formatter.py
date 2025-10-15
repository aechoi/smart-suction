"""Module for processing AD7746 switch mux board serial data files."""

import os
import numpy as np


class SerialData:
    def __init__(self, file_path: str):
        """
        Args:
            file_path:"""
        self.name = os.path.split(file_path)[1]
        self.time, self.cap_counts, self.actuations = self._read_file(file_path)
        self.sampling_period = np.mean(np.diff(self.time))

        self.actuation_starts = (
            np.where(np.diff(self.actuations.astype(int)) == 1)[0] + 1
        )
        self.actuation_ends = (
            np.where(np.diff(self.actuations.astype(int)) == -1)[0] + 1
        )
        self.segment_starts = np.r_[
            0, np.where(np.diff(self.actuations.astype(int)) == -1)[0][:-1] + 1
        ]
        self.segment_ends = np.where(np.diff(self.actuations.astype(int)) == 1)[0] + 1

    def _read_file(self, file_path: str):
        """Reads the file and extracts headers and numerical data as NumPy arrays."""
        timestamps, cap_data, actuation = [], [], []

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip()
                if not line:
                    continue

                raw_values = line.split(" ")
                if len(raw_values) != 10:
                    continue
                for raw_entry in raw_values[1:-1]:
                    if len(raw_entry) != 8:
                        break
                else:
                    values = [float(entry) for entry in raw_values]
                    timestamps.append(values[0])
                    cap_data.append(values[1:9])
                    actuation.append(values[-1])

        cap_counts = np.array(cap_data, dtype=np.int32)
        actuations = np.array(actuation, dtype=np.int32)
        timestamps = np.array(timestamps) - timestamps[0]

        return timestamps, cap_counts, actuations

    def normalize(self, data):
        """Zero the data around its mean"""
        return data - np.mean(data[: self.segment_ends[0]], axis=0)


def format_folder(folder_path: str):
    """Given a folder path, generate EvalBoardData objects for all files."""
    data_objects = []
    directory_items = sorted(os.listdir(folder_path))
    for item in directory_items:
        if item == "Settings.txt":
            continue
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            data_objects.append(SerialData(item_path))
    return data_objects
