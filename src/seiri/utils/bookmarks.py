import calendar


def create_bookmarks(app, pdf_canvas):
    """
    Create bookmarks

    Parameters:
    app (Seiri): The Seiri app.
    pdf_canvas (Canvas): The PDF canvas.
    """

    create_year_bookmark(pdf_canvas)
    create_month_bookmarks(pdf_canvas)
    create_week_bookmarks(pdf_canvas, app.year, app.first_day_of_week)


def create_year_bookmark(pdf_canvas):
    """
    Predefine bookmarks for the year.
    """

    pdf_canvas.bookmarkPage("year")


def create_month_bookmarks(pdf_canvas):
    """
    Predefine bookmarks for all months.
    """

    for month in range(1, 13):
        destination_name = f"month_{month}"
        pdf_canvas.bookmarkPage(destination_name)


def create_week_bookmarks(pdf_canvas, year, first_day_of_week):
    """
    Predefine bookmarks for all weeks.
    This accounts for the fact that a week can span two months.
    Such weeks will be bookmarked as jan_week_5_feb_week_1.
    """

    calendar.setfirstweekday(
        calendar.MONDAY if first_day_of_week == "Mon" else calendar.SUNDAY
    )

    previous_month = None
    previous_week_index = None

    for month in range(1, 13):
        days = calendar.monthcalendar(year, month)
        for week_index, week in enumerate(days):
            if previous_month is not None:
                destination_name = (
                    f"{calendar.month_abbr[previous_month].lower()}_week_{previous_week_index + 1}_"
                    f"{calendar.month_abbr[month].lower()}_week_{week_index + 1}"
                )
                previous_month = None
                previous_week_index = None
            else:
                destination_name = (
                    f"{calendar.month_abbr[month].lower()}_week_{week_index + 1}"
                )

            pdf_canvas.bookmarkPage(destination_name)

            if week[-1] == 0:
                previous_month = month
                previous_week_index = week_index
