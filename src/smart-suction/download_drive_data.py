import gdown
import os


def download_file(url: str, data_directory: str = None) -> None:
    """Downloads a file from the google drive url to a local location

    Args
        url: the sharable file link, only works if anyone with link has access
        data_directory: the location where the data will be stored. Defaults to
            a folder in the working directory called 'data/' (recommended to be
            called data b/c .gitignore won't push it to the repo.)
    """
    if data_directory is None:
        data_directory = os.path.join(os.getcwd(), "data")

    gdown.download(url, quiet=False)


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
        data_directory = os.path.join(os.getcwd(), "data")

    file_list = gdown.download_folder(url, skip_download=True)
    potential_duplicate, folder_directory = check_if_downloaded(
        file_list, data_directory
    )
    if potential_duplicate:
        raise FileExistsError(
            "It's possible you've already downloaded this data. If so, delete and try again."
        )
    gdown.download_folder(url, output=folder_directory, quiet=False)


def check_if_downloaded(file_list: list[str], data_directory: str) -> tuple[bool, str]:
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
    potential_duplicate = False
    for file in file_list:
        _, folder_name = os.path.split(os.path.dirname(file.local_path))
        folder_directory = os.path.join(data_directory, folder_name)
        if file.path in os.listdir(folder_directory):
            potential_duplicate = True

    return potential_duplicate, folder_directory


if __name__ == "__main__":
    url = "https://drive.google.com/drive/folders/1iJHOh6pBJC13yKVfcgykayG_F2aS1bvn?usp=drive_link"
    download_folder(url)
