from reportlab.pdfgen import canvas

from seiri.utils import logging
from seiri.utils.create_months import insert_months
from seiri.utils.create_year import insert_year
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
            f"Device Height:        {app.device_height}px\n"
            f"Device Width:         {app.device_width}px\n"
            f"Top Margin:           {app.margin_top}px\n"
            f"Right Margin:         {app.margin_right}px\n"
            f"Bottom Margin:        {app.margin_bottom}px\n"
            f"Left Margin:          {app.margin_left}px\n"
            f"Selected Year:        {app.year}\n"
            f"First Day of Week:    {app.first_day_of_week}\n"
            f"Layout:               {app.layout}\n"
        )
        logger.info(options_selected)

        if app.layout == "Tall":
            page_width, page_height = app.device_width, app.device_height
        else:
            page_width, page_height = app.device_height, app.device_width

        pdf_canvas = canvas.Canvas(
            str(app.pdf_path), pagesize=(page_width, page_height)
        )
        insert_year(app, pdf_canvas)
        insert_months(app, pdf_canvas)
        pdf_canvas.save()

    except Exception:
        logger.exception("Failed to create the PDF file.")
