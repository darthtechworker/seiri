from datetime import datetime

import toga
from toga.style.pack import BOLD, COLUMN, ROW, Pack

SELECT_YEAR_LABEL = "Select Year:"


def build_select_year_container(app):
    """
    Build the select year container.
    """

    app.select_year_label = toga.Label(
        text=SELECT_YEAR_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 54, 0, 0)),
    )
    current_year = datetime.now().year
    next_year = current_year + 1
    app.year_dropdown = toga.Selection(
        items=[current_year, next_year],
        style=Pack(width=67),
        on_change=lambda widget: on_change_year_dropdown(widget, app),
    )

    app.select_year_container = toga.Box(style=Pack(direction=ROW))
    app.select_year_container.add(app.select_year_label)
    app.select_year_container.add(app.year_dropdown)


def on_change_year_dropdown(widget, app):
    """
    Handle the change event on the year dropdown.
    """

    widget.on_change = None
    app.year = int(widget.value) if widget.value else None
    widget.on_change = lambda widget: on_change_year_dropdown(widget, app)


def build_year_options_container(app):
    """
    Build the year options container.
    """

    build_select_year_container(app)

    app.year_options_container = toga.Box(
        style=Pack(direction=COLUMN, alignment="center", padding=(10, 0, 10, 0))
    )
    app.year_options_container.add(app.select_year_container)

    return app.year_options_container
