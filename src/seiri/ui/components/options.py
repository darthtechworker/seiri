import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from seiri.ui.components.select_output_directory import (
    build_select_output_directory_button,
)


def build_options_container(app):
    """
    Build the options container.
    """

    build_select_output_directory_button(app)

    app.options_container = toga.Box(style=Pack(direction=COLUMN, flex=1))
    app.options_container.add(app.select_output_directory_button)

    return app.options_container
