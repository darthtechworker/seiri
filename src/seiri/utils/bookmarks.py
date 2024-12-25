def create_bookmarks(app, pdf_canvas):
    """
    Create bookmarks

    Parameters:
    app (Seiri): The Seiri app.
    pdf_canvas (Canvas): The PDF canvas.
    """

    create_year_bookmark(pdf_canvas)
    create_month_bookmarks(pdf_canvas)


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
