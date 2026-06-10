"""Module for processing PCAP01 eval board data into capacitance data"""

import os
import re
import numpy as np


class SciosenseCapData:
    """An object defining a single data collection done on the PCAP01 eval
    board. It is unknown whether the format of the eval board output is
    consistent, so the code for managing the header may not be correct in
    general.

    """

    def __init__(self, file_path: str, sampling_rate: float = 14.3):
        """
        Args:
            file_path:"""
        self.trial_name = os.path.split(file_path)[1]
        self.data_label, self.cap_counts = self._read_file(file_path)
        self.sampling_period = 1 / sampling_rate
        self.time = np.arange(
            0, len(self.cap_counts) * self.sampling_period, self.sampling_period
        )

    def _read_file(self, file_path: str):
        """Reads the file and extracts headers and numerical data as NumPy arrays."""
        data_label = ""
        data_start = False
        cap_data = []

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip()
                if not line:
                    continue

                if not data_start:
                    # Handle headers (only care about parameters, ie where ":" are)
                    data_label = line
                else:
                    # Parse data section
                    data_columns = line.split("\t")
                    cap_data.append(float(data_columns[0]))

                if not data_start and re.match(
                    r"^%C\d+/C\d+$", line
                ):  # Detects hexadecimal rows (data section)
                    data_start = True

        cap_counts = np.array(cap_data)

        return data_label, cap_counts


def format_folder(folder_path: str):
    """Given a folder path, generate EvalBoardData objects for all files."""
    data_objects = []
    directory_items = sorted(os.listdir(folder_path))
    for item in directory_items:
        if item == "Settings.txt":
            continue
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            data_objects.append(SciosenseCapData(item_path))
    return data_objects
