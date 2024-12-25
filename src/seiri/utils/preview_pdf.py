import os

import fitz

from seiri.utils.file import cleanup_directory


def get_number_of_pages(app):
    """
    Get the number of pages in a PDF file.

    Parameters:
    app (Seiri): The Seiri app.

    Returns:
    int: The number of pages.
    """

    pdf_document = fitz.open(app.pdf_path)
    number_of_pages = len(pdf_document)
    pdf_document.close()

    return number_of_pages


def convert_pdf_to_images(app, page_num):
    """
    Convert a page from a PDF file to an image.

    Parameters:
    app (Seiri): The Seiri app.
    page_num (int): The page number.

    Returns:
    str: The path of the image.
    """

    cleanup_directory(app.working_directory)

    pdf_document = fitz.open(app.pdf_path)
    page = pdf_document.load_page(page_num)
    pix = page.get_pixmap()
    image_path = os.path.join(app.working_directory, f"Page {page_num}.png")
    pix.save(image_path)
    pdf_document.close()

    return image_path
