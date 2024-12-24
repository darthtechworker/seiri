import calendar

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
            f"Device Height:        {app.device_height}px\n"
            f"Device Width:         {app.device_width}px\n"
            f"Top Margin:           {app.margin_top}px\n"
            f"Right Margin:         {app.margin_right}px\n"
            f"Bottom Margin:        {app.margin_bottom}px\n"
            f"Left Margin:          {app.margin_left}px\n"
            f"Selected Year:        {app.year}\n"
        )
        logger.info(options_selected)

        page_width, page_height = app.device_width, app.device_height
        pdf_canvas = canvas.Canvas(
            str(app.pdf_path), pagesize=(page_width, page_height)
        )
        insert_year_view(app, pdf_canvas)
        pdf_canvas.save()

    except Exception:
        logger.exception("Failed to create the PDF file.")


def insert_year_view(app, pdf_canvas):
    """
    Insert the year view into the PDF file.
    """

    try:
        year = app.year

        cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
        months = calendar.month_name[1:]
        days_of_week = ["M", "T", "W", "T", "F", "S", "S"]
        month_font_size = 35
        padding_between_months = 20

        usable_width = app.device_width - app.margin_left - app.margin_right
        usable_height = app.device_height - app.margin_top - app.margin_bottom

        month_width = (usable_width - 2 * padding_between_months) / 3
        month_height = (usable_height - 3 * padding_between_months) / 4

        vertical_spacing = month_height / 8
        horizontal_spacing = month_width / 7

        x_offset = app.margin_left
        y_offset = (
            app.device_height - app.margin_top - month_font_size
        )  # Adjust for the font size as reportlabs draws text from the bottom left corner

        for month_index, month_name in enumerate(months):
            x = x_offset + (month_index % 3) * (month_width + padding_between_months)
            y = y_offset - (month_index // 3) * (month_height + padding_between_months)

            pdf_canvas.setFont("Helvetica", month_font_size)
            pdf_canvas.drawString(x, y, month_name)

            day_x = x
            day_y = y - vertical_spacing

            pdf_canvas.setFont("Helvetica", 25)
            for day in days_of_week:
                pdf_canvas.drawString(day_x, day_y, day)
                day_x += horizontal_spacing

            day_y -= vertical_spacing

            days = cal.monthdayscalendar(year, month_index + 1)
            for week in days:
                day_x = x
                for day in week:
                    if day != 0:
                        pdf_canvas.drawString(day_x, day_y, str(day))
                    day_x += horizontal_spacing
                day_y -= vertical_spacing

        pdf_canvas.showPage()

    except Exception:
        logger.exception("Failed to insert the year view into the PDF file.")
