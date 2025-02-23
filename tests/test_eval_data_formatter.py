"""Test functions and class methods in eval_data_formatter.py"""

import os

import capcup.eval_data_formatter as edf


def test_EvalBoardData():
    data_path = os.path.join(os.getcwd(), "tests", "data", "test_eval_data.txt")
    test_data_obj = edf.EvalBoardData(data_path)
    assert len(test_data_obj.cap_array) == 1296
    assert test_data_obj.sampling_period == 0.062
    assert test_data_obj.headers["Channel"] == "1"
    assert test_data_obj.headers["Mode"] == "Single-Ended"
    assert test_data_obj.headers["Chop"] == "Off"
    assert test_data_obj.headers["CAP DAC A"] == "Disabled"
    assert test_data_obj.headers["CAP DAC B"] == "Disabled"


def test_format_folder():
    folder_path = os.path.join(os.getcwd(), "tests", "data")
    trial_list = edf.format_folder(folder_path)

    for trial in trial_list:
        assert trial.sampling_period == 0.062
        assert trial.headers["Channel"] == "1"
        assert trial.headers["Mode"] == "Single-Ended"
        assert trial.headers["Chop"] == "Off"
        assert trial.headers["CAP DAC A"] == "Disabled"
        assert trial.headers["CAP DAC B"] == "Disabled"
