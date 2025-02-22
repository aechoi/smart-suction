"""Unit tests for download_drive_data.py

Google restricts access to a file when downloaded too much. Using cookies can
help as described here https://github.com/wkentaro/gdown?tab=readme-ov-file#faq
or you can just wait a bit.
"""

import os
import pytest

import capcup.download_drive_data as down


def test_download_file():
    test_file_url = "https://drive.google.com/file/d/1GkTkqgJF6GOn8fSytB2M81oCj3ZqKVLY/view?usp=sharing"
    down.download_file(test_file_url)

    # Check if downloaded, if so, delete
    expected_directory = os.path.join(os.getcwd(), "data")
    expected_file = os.path.join(expected_directory, "test_file_1.txt")
    assert os.path.isfile(expected_file)
    os.remove(expected_file)
    assert not os.path.isfile(expected_file)
    try:
        os.rmdir(expected_directory)
        assert not os.path.isdir(expected_directory)
    except OSError:
        pass


def test_download_file_to_directory():
    test_file_url = "https://drive.google.com/file/d/1GkTkqgJF6GOn8fSytB2M81oCj3ZqKVLY/view?usp=sharing"

    expected_directory = os.path.join(os.getcwd(), "temp_test")
    down.download_file(test_file_url, data_directory=expected_directory)

    # Check if downloaded, if so, delete
    expected_file = os.path.join(expected_directory, "test_file_1.txt")
    assert os.path.isfile(expected_file)
    os.remove(expected_file)
    os.rmdir(expected_directory)
    assert not os.path.isfile(expected_file)
    assert not os.path.isdir(expected_directory)


def test_download_folder():
    test_folder_url = "https://drive.google.com/drive/folders/1wViKlt6hXWR0qlF4bl8enXwWyjzeBXot?usp=drive_link"

    down.download_folder(test_folder_url)

    expected_directory = os.path.join(os.getcwd(), "data", "test_folder")
    expected_files = [
        os.path.join(expected_directory, "test_file_1.txt"),
        os.path.join(expected_directory, "test_file_2.txt"),
    ]

    for file in expected_files:
        assert os.path.isfile(file)

    # Attempt duplicate download
    with pytest.raises(FileExistsError):
        down.download_folder(test_folder_url)

    # Remove files and directories
    for file in expected_files:
        os.remove(file)
        assert not os.path.isfile(file)
    try:
        os.rmdir(expected_directory)
        assert not os.path.isdir(expected_directory)

        data_directory, _ = os.path.split(expected_directory)
        os.rmdir(data_directory)
        assert not os.path.isdir(data_directory)
    except OSError:
        pass


def test_download_folder_to_directory():
    test_folder_url = "https://drive.google.com/drive/folders/1wViKlt6hXWR0qlF4bl8enXwWyjzeBXot?usp=drive_link"

    expected_directory = os.path.join(os.getcwd(), "data", "test_folder_new")
    down.download_folder(test_folder_url, data_directory=expected_directory)
    expected_directory = os.path.join(expected_directory, "test_folder")

    expected_files = [
        os.path.join(expected_directory, "test_file_1.txt"),
        os.path.join(expected_directory, "test_file_2.txt"),
    ]

    for file in expected_files:
        assert os.path.isfile(file)

    # Remove files and directories
    for file in expected_files:
        os.remove(file)
        assert not os.path.isfile(file)
    try:
        os.removedirs(expected_directory)
        assert not os.path.isdir(expected_directory)

        # data_directory, _ = os.path.split(expected_directory)
        # os.rmdir(data_directory)
        # assert not os.path.isdir(data_directory)
    except OSError:
        pass
