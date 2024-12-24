import os
import platform
import re
import subprocess
import unicodedata

from seiri.utils import logging

logger = logging.getLogger(__name__)


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
