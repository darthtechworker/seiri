from datetime import datetime

import toga
from toga.style.pack import BOLD, COLUMN, ROW, Pack

SELECT_YEAR_LABEL = "Select Year:"
FIRST_DAY_OF_WEEK_LABEL = "First Day of Week:"


def build_select_year_container(app):
    """
    Build the select year container.
    """

    app.select_year_label = toga.Label(
        text=SELECT_YEAR_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 52, 0, 0)),
    )
    current_year = datetime.now().year
    next_year = current_year + 1
    app.year_dropdown = toga.Selection(
        items=[current_year, next_year],
        style=Pack(width=67),
        on_change=lambda widget: on_change_year_dropdown(widget, app),
    )

    app.select_year_container = toga.Box(
        style=Pack(direction=ROW, padding=(0, 0, 10, 0))
    )
    app.select_year_container.add(app.select_year_label)
    app.select_year_container.add(app.year_dropdown)


def on_change_year_dropdown(widget, app):
    """
    Handle the change event on the year dropdown.
    """

    widget.on_change = None
    app.year = int(widget.value) if widget.value else None
    widget.on_change = lambda widget: on_change_year_dropdown(widget, app)


def build_first_day_of_week_container(app):
    """
    Build the first day of week container.
    """

    app.first_day_of_week_label = toga.Label(
        text=FIRST_DAY_OF_WEEK_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 13, 0, 0)),
    )
    app.first_day_of_week_dropdown = toga.Selection(
        items=["Sun", "Mon"],
        style=Pack(width=67),
        on_change=lambda widget: on_change_first_day_of_week_dropdown(widget, app),
    )

    app.first_day_of_week_container = toga.Box(style=Pack(direction=ROW))
    app.first_day_of_week_container.add(app.first_day_of_week_label)
    app.first_day_of_week_container.add(app.first_day_of_week_dropdown)


def on_change_first_day_of_week_dropdown(widget, app):
    """
    Handle the change event on the first day of week dropdown.
    """

    widget.on_change = None
    app.first_day_of_week = widget.value
    widget.on_change = lambda widget: on_change_first_day_of_week_dropdown(widget, app)


def build_calendar_options_container(app):
    """
    Build the calendar options container.
    """

    build_select_year_container(app)
    build_first_day_of_week_container(app)

    app.calendar_options_container = toga.Box(
        style=Pack(direction=COLUMN, alignment="center", padding=(10, 0, 10, 0))
    )

    app.calendar_options_container.add(app.select_year_container)
    app.calendar_options_container.add(app.first_day_of_week_container)
