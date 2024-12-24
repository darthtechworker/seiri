from reportlab.pdfgen import canvas

from seiri.utils import logging
from seiri.utils.file import create_directory

logger = logging.getLogger(__name__)


def create_pdf(app):
    """
    Create a PDF file with the given filename.
    """

    try:
        create_directory(app.output_directory)
        create_directory(app.working_directory)

        app.pdf_path = app.working_directory / "output.pdf"

        options_selected = (
            f"\n\n\nOptions Selected:\n\n"
            f"Output Directory:     {app.output_directory}\n"
            f"Working Directory:    {app.working_directory}\n"
            f"PDF Path:             {app.pdf_path}\n"
        )
        logger.info(options_selected)

        page_width, page_height = 1404, 1872
        c = canvas.Canvas(str(app.pdf_path), pagesize=(page_width, page_height))
        for page_number in range(1, 900):
            c.drawString(
                100,
                page_height - 100,
                f"This is page {page_number} of size 1404 × 1872.",
            )
            c.showPage()
        c.save()

    except Exception:
        logger.exception(f"Failed to create a PDF file: {app.pdf_path}")
