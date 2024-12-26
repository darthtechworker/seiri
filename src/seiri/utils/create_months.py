import calendar

from seiri.utils import logging
from seiri.utils.font_utils import get_font_scale_factor

logger = logging.getLogger(__name__)


def insert_months(app, pdf_canvas):
    """
    Insert the month view into the PDF file.
    """

    try:
        if app.first_day_of_week == "Mon":
            cal = calendar.Calendar(firstweekday=calendar.MONDAY)
            days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        else:
            cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
            days_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

        font_scale_factor = get_font_scale_factor(app)

        breadcrumb_font = "Helvetica-Bold"
        breadcrumb_font_size = 40 * font_scale_factor
        week_font = "Helvetica"
        day_of_week_font_size = 30 * font_scale_factor
        day_font = "Helvetica"
        day_font_size = 30 * font_scale_factor

        if app.layout == "Tall":
            usable_width = app.device_width - app.margin_left - app.margin_right
            usable_height = app.device_height - app.margin_top - app.margin_bottom
        else:
            usable_width = app.device_height - app.margin_top - app.margin_bottom
            usable_height = app.device_width - app.margin_left - app.margin_right

        day_width = usable_width / 7
        day_height = usable_height / 7

        vertical_spacing = usable_height / 7

        if app.layout == "Tall":
            x_offset = app.margin_left
            y_offset = app.device_height - app.margin_top - breadcrumb_font_size
        else:
            x_offset = app.margin_top
            y_offset = app.device_width - app.margin_left - breadcrumb_font_size

        for month in range(1, 13):
            destination_name = f"month_{month}"
            pdf_canvas.bookmarkPage(destination_name)

            pdf_canvas.setFont(breadcrumb_font, breadcrumb_font_size)
            year_name = str(app.year)
            pdf_canvas.drawString(x_offset, y_offset, year_name)

            year_text_width = pdf_canvas.stringWidth(
                year_name, breadcrumb_font, breadcrumb_font_size
            )
            pdf_canvas.linkRect(
                contents="Go to year",
                destinationname="year",
                Rect=(
                    x_offset,
                    y_offset,
                    x_offset + year_text_width,
                    y_offset + breadcrumb_font_size,
                ),
                relative=0,
            )

            separator = " - "
            text_width = pdf_canvas.stringWidth(
                year_name, breadcrumb_font, breadcrumb_font_size
            )
            pdf_canvas.drawString(x_offset + text_width, y_offset, separator)

            month_name = calendar.month_name[month]
            text_width += pdf_canvas.stringWidth(
                separator, breadcrumb_font, breadcrumb_font_size
            )
            pdf_canvas.drawString(x_offset + text_width, y_offset, month_name)

            day_of_week_y = y_offset - (vertical_spacing / 4)

            pdf_canvas.setFont(week_font, day_of_week_font_size)
            for i, day in enumerate(days_of_week):
                day_center_x = x_offset + (i * day_width) + (day_width / 2)
                text_width = pdf_canvas.stringWidth(
                    day, week_font, day_of_week_font_size
                )
                pdf_canvas.drawString(day_center_x - text_width / 2, day_of_week_y, day)

            day_y = day_of_week_y - (vertical_spacing / 4)

            pdf_canvas.setFont(day_font, day_font_size)
            days = cal.monthdayscalendar(app.year, month)
            for week in days:
                for i, day in enumerate(week):
                    if day != 0:
                        day_center_x = x_offset + (i * day_width)
                        pdf_canvas.drawString(
                            day_center_x + day_font_size / 4,
                            day_y - day_font_size,
                            str(day),
                        )
                        pdf_canvas.rect(
                            day_center_x, day_y - day_height, day_width, day_height
                        )
                day_y -= day_height

            pdf_canvas.showPage()

    except Exception:
        logger.exception("Failed to insert the month view into the PDF file.")
