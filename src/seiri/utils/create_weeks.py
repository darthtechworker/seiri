import calendar

from seiri.utils import logging
from seiri.utils.font_utils import get_font_scale_factor

logger = logging.getLogger(__name__)


def insert_weeks(app, pdf_canvas):
    """
    Insert the week view into the PDF file.
    """

    try:
        if app.first_day_of_week == "Mon":
            cal = calendar.Calendar(firstweekday=calendar.MONDAY)
            days_of_week = [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ]
        else:
            cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
            days_of_week = [
                "Sunday",
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
            ]
        font_scale_factor = get_font_scale_factor(app)

        breadcrumb_font = "Helvetica-Bold"
        breadcrumb_font_size = 40 * font_scale_factor
        padding_for_breakcrumb = 2 * breadcrumb_font_size
        day_font = "Helvetica"
        day_font_size = 30 * font_scale_factor

        if app.layout == "Tall":
            usable_width = app.device_width - app.margin_left - app.margin_right
            usable_height = app.device_height - app.margin_top - app.margin_bottom
        else:
            usable_width = app.device_height - app.margin_top - app.margin_bottom
            usable_height = app.device_width - app.margin_left - app.margin_right

        day_width = usable_width / 2
        day_height = (usable_height - padding_for_breakcrumb) / 4

        if app.layout == "Tall":
            x_offset = app.margin_left
            y_offset = app.device_height - app.margin_top - breadcrumb_font_size
        else:
            x_offset = app.margin_top
            y_offset = app.device_width - app.margin_left - breadcrumb_font_size

        for month in range(1, 13):
            days = cal.monthdayscalendar(app.year, month)
            for week_index, week in enumerate(days):
                # Todo: Implement the bookmarking of the weeks.

                pdf_canvas.setFont(breadcrumb_font, breadcrumb_font_size)
                breadcrumb_text = (
                    f"{app.year} - {calendar.month_name[month]} - Week {week_index + 1}"
                )
                pdf_canvas.drawString(x_offset, y_offset, breadcrumb_text)

                day_y = y_offset - breadcrumb_font_size

                pdf_canvas.setFont(day_font, day_font_size)
                for row in range(4):
                    for col in range(2):
                        day_index = row * 2 + col
                        if day_index < len(days_of_week):
                            day = days_of_week[day_index]
                            day_center_x = x_offset + (col * day_width)
                            day_center_y = day_y - (row * day_height)
                            pdf_canvas.drawString(
                                day_center_x + day_font_size / 4,
                                day_center_y - day_font_size,
                                day,
                            )
                            pdf_canvas.rect(
                                day_center_x,
                                day_center_y - day_height,
                                day_width,
                                day_height,
                            )

                pdf_canvas.showPage()

    except Exception:
        logger.exception("Failed to insert the week view into the PDF file.")
