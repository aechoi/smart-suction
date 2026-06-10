"""Methods for downloading files and folders from google drive."""

import os

import gdown


def download_file(url: str, data_directory: str = None) -> None:
    """Downloads a file from the google drive url to a local location

    Args
        url: the sharable file link, only works if anyone with link has access
        data_directory: the location where the data will be stored. Defaults to
            a folder in the working directory called 'data/' (recommended to be
            called data b/c .gitignore won't push it to the repo.)
    """
    if data_directory is None:
        data_directory = os.path.join(os.getcwd(), "data", "")
    if data_directory[-1] != "/":
        data_directory = os.path.join(data_directory, "")

    if not os.path.isdir(data_directory):
        os.mkdir(data_directory)

    gdown.download(url, output=data_directory, quiet=False, fuzzy=True)


def download_folder(url: str, data_directory: str = None) -> None:
    """Downloads a folder from the google drive url to a local location. Will
    check if the folder has already been downloaded.

    Args
        url: the sharable file link, only works if anyone with link has access
        data_directory: the location where the data will be stored. Defaults to
            a folder in the working directory called 'data/' (recommended to be
            called data b/c .gitignore won't push it to the repo.)

    Raises
        FileExistsError: if a folder already exists in the data directory with
            the same name as the google drive folder, then it will not be
            downloaded
    """

    if data_directory is None:
        data_directory = os.path.join(os.getcwd(), "data", "")

    if data_directory[-1] != "/":
        data_directory = os.path.join(data_directory, "")

    if not os.path.isdir(data_directory):
        os.makedirs(data_directory)

    file_list = gdown.download_folder(url, skip_download=True)
    _, folder_name = os.path.split(os.path.dirname(file_list[0].local_path))
    folder_directory = os.path.join(data_directory, folder_name)

    if check_if_downloaded(file_list, folder_directory):
        raise FileExistsError(
            "It's possible you've already downloaded this data. If so, delete and try again."
        )
    gdown.download_folder(url, output=folder_directory, quiet=False)


def check_if_downloaded(
    file_list: list[str], folder_directory: str
) -> tuple[bool, str]:
    """Checks if a list of files already exists with the same folder name

    Args:
        file_list: the output of gdown.download_folder with skip_download set
            to True
        data_directory: the directory named 'data/' that has all the
            subdirectories to check the name against

    Returns:
        a boolean true/false depending on whether a duplicate was found, and
        the full path to the folder's local download location (ie. one level
        deeper than the 'data/' directory)"""
    if not os.path.isdir(folder_directory):
        # the directory does not exist, so no chance of duplicate
        return False

    potential_duplicate = False
    for file in file_list:
        if file.path in os.listdir(folder_directory):
            potential_duplicate = True

    return potential_duplicate
