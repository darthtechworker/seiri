import asyncio

import toga
from toga.style.pack import BOLD, COLUMN, Pack

SELECT_OUTPUT_DIRECTORY_LABEL = "Select Output Directory"


def build_select_output_directory_button(app):
    """
    Build the select output directory button.
    """

    app.select_output_directory_button = toga.Button(
        SELECT_OUTPUT_DIRECTORY_LABEL,
        on_press=lambda widget: asyncio.ensure_future(
            on_click_select_output_directory(widget, app)
        ),
        style=Pack(font_weight=BOLD, height=30, width=200),
    )


async def on_click_select_output_directory(widget, app):
    """
    Handle the click event on the select output directory button.
    """

    dialog = toga.SelectFolderDialog(
        title=SELECT_OUTPUT_DIRECTORY_LABEL,
        initial_directory=None,
        multiple_select=None,
    )
    selected_folder = await dialog._show(app.main_window)

    if selected_folder is not None:
        app.output_directory = selected_folder
        app.working_directory = app.output_directory / ".tmp"
        app.preview_button.enabled = True


def build_select_output_directory_container(app):
    """
    Build the select output directory container.
    """

    build_select_output_directory_button(app)

    app.select_output_directory_container = toga.Box(
        style=Pack(direction=COLUMN, alignment="center", padding=(20, 0, 10, 0))
    )
    app.select_output_directory_container.add(app.select_output_directory_button)
