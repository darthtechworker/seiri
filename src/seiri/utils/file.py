import os
import platform
import re
import subprocess
import unicodedata
from typing import List

from seiri.utils import logging

logger = logging.getLogger(__name__)

SUPPORTED_IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png"]


def create_directory(directory_path: str) -> None:
    """
    Create a directory if it does not already exist.

    Parameters:
    directory_path (str): The path of the directory to create.
    """

    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def sanitize_title(title: str, max_length: int = 100) -> str:
    """
    Sanitizes a title for use as a filename.

    Parameters:
    title (str): The title to sanitize.

    Returns:
    str: A sanitized filename-safe title.
    """

    title = unicodedata.normalize("NFC", title)

    title = re.sub(r'[<>:"/\\|?*\n\r\t]', "_", title)

    title = "".join(char for char in title if char.isprintable())

    title = title.strip(" .")

    if len(title) > max_length:
        title = title[:max_length].rstrip(" .")

    reserved_names = {
        "CON",
        "PRN",
        "AUX",
        "NUL",
        "COM1",
        "COM2",
        "COM3",
        "COM4",
        "COM5",
        "COM6",
        "COM7",
        "COM8",
        "COM9",
        "LPT1",
        "LPT2",
        "LPT3",
        "LPT4",
        "LPT5",
        "LPT6",
        "LPT7",
        "LPT8",
        "LPT9",
    }
    if title.upper() in reserved_names:
        title += "_file"

    return title


def open_directory_in_ui(directory_path: str) -> None:
    """
    Open the directory in the file explorer.

    Parameters:
    directory_path (str): The path of the directory to open.
    """

    system = platform.system()

    if system == "Darwin":  # macOS
        subprocess.run(["open", directory_path], check=True)
    elif system == "Windows":  # Windows
        os.startfile(directory_path)
    elif system == "Linux":  # Linux
        subprocess.run(["xdg-open", directory_path], check=True)
    else:
        print(f"Unsupported operating system: {system}")


def get_supported_images(directory_path) -> List[str]:
    """
    Get the supported images.

    Parameters:
    directory_path (str): The path of the directory containing the images.

    Returns:
    List[str]: The sorted names of the supported images.
    """

    image_names = []
    for image_name in os.listdir(directory_path):
        if image_name.lower().endswith(tuple(SUPPORTED_IMAGE_EXTENSIONS)):
            image_names.append(image_name)

    image_names.sort()

    return image_names


def cleanup_directory(directory_path: str) -> None:
    """
    Cleanup the directory by removing all images in it.

    Parameters:
    directory_path (str): The path of the directory to cleanup.
    """

    for file_name in os.listdir(directory_path):
        if file_name.lower().endswith(tuple(SUPPORTED_IMAGE_EXTENSIONS)):
            os.remove(os.path.join(directory_path, file_name))
