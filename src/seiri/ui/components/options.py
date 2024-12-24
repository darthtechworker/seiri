import toga
from toga.style import Pack
from toga.style.pack import COLUMN

from seiri.ui.components.general_options import build_general_options_container
from seiri.ui.components.select_output_directory import (
    build_select_output_directory_container,
)
from seiri.ui.components.year_options import build_year_options_container


def build_options_container(app):
    """
    Build the options container.
    """

    build_select_output_directory_container(app)
    build_general_options_container(app)
    build_year_options_container(app)

    app.options_container = toga.Box(
        style=Pack(direction=COLUMN, flex=1, alignment="center")
    )
    app.options_container.add(app.select_output_directory_container)
    app.options_container.add(app.general_options_container)
    app.options_container.add(app.year_options_container)

    return app.options_container
