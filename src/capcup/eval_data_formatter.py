"""Module for processing AD7746 eval board data into capacitance data"""

import os
import re
import numpy as np


class EvalBoardData:
    """An object defining a single data collection done on the AD7746 eval
    board. It is unknown whether the format of the eval board output is
    consistent, so the code for managing the header may not be correct in
    general.

    """

    def __init__(self, file_path: str):
        """
        Args:
            file_path:"""
        self.trial_name = os.path.split(file_path)[1]
        self.headers, self.cap_counts, self.volt_temp_data = self._read_file(file_path)
        self.sampling_period = float(self.headers["Conv. Time"].split()[0]) / 1000
        self.time = np.arange(
            0, len(self.cap_counts) * self.sampling_period, self.sampling_period
        )

    def _read_file(self, file_path: str):
        """Reads the file and extracts headers and numerical data as NumPy arrays."""
        headers = {}
        data_start = False
        cap_data, volt_temp_data = [], []

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip()
                if not line:
                    continue

                if not data_start and re.match(
                    r"^[0-9A-F]+\s+[0-9A-F]+$", line
                ):  # Detects hexadecimal rows (data section)
                    data_start = True

                if not data_start:
                    # Handle headers (only care about parameters, ie where ":" are)
                    if ":" in line:
                        configs = line.split("\t")
                        for config in configs:
                            key, value = map(str.strip, config.split(":"))
                            headers[key] = value
                else:
                    # Parse data section
                    data_columns = line.split("\t")
                    cap_data.append(int(data_columns[0], 16))
                    volt_temp_data.append(int(data_columns[1], 16))

        cap_counts = np.array(cap_data, dtype=np.int32)
        volt_temp_array = np.array(volt_temp_data, dtype=np.int32)

        return headers, cap_counts, volt_temp_array


def format_folder(folder_path: str):
    """Given a folder path, generate EvalBoardData objects for all files."""
    data_objects = []
    directory_items = os.listdir(folder_path)
    for item in directory_items:
        if item == "Settings.txt":
            continue
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            data_objects.append(EvalBoardData(item_path))
    return data_objects
