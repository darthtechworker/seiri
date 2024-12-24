import os

import fitz

from seiri.utils.file import cleanup_directory


def convert_pdf_to_images(app):
    """
    Convert a PDF file to a list of images.
    """

    cleanup_directory(app.working_directory)

    pdf_document = fitz.open(app.pdf_path)
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()
        image_path = os.path.join(app.working_directory, f"Page {page_num + 1:04d}.png")
        pix.save(image_path)
