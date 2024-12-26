import calendar

from seiri.utils import logging
from seiri.utils.font_utils import get_font_scale_factor

logger = logging.getLogger(__name__)


def insert_year(app, pdf_canvas):
    """
    Insert the year view into the PDF file.
    """

    try:
        destination_name = "year"
        pdf_canvas.bookmarkPage(destination_name)

        if app.first_day_of_week == "Mon":
            cal = calendar.Calendar(firstweekday=calendar.MONDAY)
            days_of_week = ["M", "T", "W", "T", "F", "S", "S"]
        else:
            cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
            days_of_week = ["S", "M", "T", "W", "T", "F", "S"]

        font_scale_factor = get_font_scale_factor(app)

        year_font = "Helvetica-Bold"
        year_font_size = 50 * font_scale_factor
        months = calendar.month_name[1:]
        month_font = "Helvetica-Bold"
        month_font_size = 35 * font_scale_factor
        week_font = "Helvetica"
        day_of_week_font_size = 25 * font_scale_factor
        day_font = "Helvetica"
        day_font_size = 25 * font_scale_factor
        padding = 30 * font_scale_factor

        if app.layout == "Tall":
            usable_width = app.device_width - app.margin_left - app.margin_right
            usable_height = (
                app.device_height
                - app.margin_top
                - app.margin_bottom
                - year_font_size
                - 2 * padding
            )
            month_width = (usable_width - 2 * padding) / 3
            month_height = (usable_height - 3 * padding) / 4
        else:
            usable_width = app.device_height - app.margin_top - app.margin_bottom
            usable_height = (
                app.device_width
                - app.margin_left
                - app.margin_right
                - year_font_size
                - 2 * padding
            )
            month_width = (usable_width - 3 * padding) / 4
            month_height = (usable_height - 2 * padding) / 3

        vertical_spacing = month_height / 8

        x_offset = app.margin_left
        if app.layout == "Tall":
            y_offset = app.device_height - app.margin_top - year_font_size
        else:
            y_offset = app.device_width - app.margin_top - year_font_size

        pdf_canvas.setFont(year_font, year_font_size)
        year_text = str(app.year)
        year_text_width = pdf_canvas.stringWidth(year_text, year_font, year_font_size)
        year_center_x = x_offset + (usable_width / 2)
        pdf_canvas.drawString(year_center_x - year_text_width / 2, y_offset, year_text)

        y_offset -= year_font_size + padding

        for month_index, month_name in enumerate(months):
            if app.layout == "Tall":
                month_x = x_offset + (month_index % 3) * (month_width + padding)
                month_y = y_offset - (month_index // 3) * (month_height + padding)
            else:
                month_x = x_offset + (month_index % 4) * (month_width + padding)
                month_y = y_offset - (month_index // 4) * (month_height + padding)

            pdf_canvas.setFont(month_font, month_font_size)
            text_width = pdf_canvas.stringWidth(month_name, month_font, month_font_size)
            center_x = month_x + (month_width / 2)
            pdf_canvas.drawString(center_x - text_width / 2, month_y, month_name)

            link_x1 = center_x - text_width / 2
            link_y1 = month_y + month_font_size
            link_x2 = center_x + text_width / 2
            link_y2 = month_y
            destination_name = f"month_{month_index + 1}"
            pdf_canvas.linkRect(
                contents=f"Go to {month_name}",
                destinationname=destination_name,
                Rect=(link_x1, link_y1, link_x2, link_y2),
                relative=0,
            )

            day_of_week_y = month_y - vertical_spacing

            pdf_canvas.setFont(week_font, day_of_week_font_size)
            for i, day in enumerate(days_of_week):
                day_center_x = month_x + (i * (month_width / 7)) + (month_width / 14)
                text_width = pdf_canvas.stringWidth(
                    day, week_font, day_of_week_font_size
                )
                pdf_canvas.drawString(day_center_x - text_width / 2, day_of_week_y, day)

            day_y = day_of_week_y - vertical_spacing

            pdf_canvas.setFont(day_font, day_font_size)
            days = cal.monthdayscalendar(app.year, month_index + 1)
            for week in days:
                for i, day in enumerate(week):
                    if day != 0:
                        day_center_x = (
                            month_x + (i * (month_width / 7)) + (month_width / 14)
                        )
                        text_width = pdf_canvas.stringWidth(
                            str(day), day_font, day_font_size
                        )
                        pdf_canvas.drawString(
                            day_center_x - text_width / 2, day_y, str(day)
                        )
                day_y -= vertical_spacing

        pdf_canvas.showPage()

    except Exception:
        logger.exception("Failed to insert the year view into the PDF file.")
