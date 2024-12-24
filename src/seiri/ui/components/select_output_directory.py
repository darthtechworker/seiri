import asyncio

import toga
from toga.style.pack import BOLD, Pack

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
        style=Pack(font_weight=BOLD, padding=(20, 80, 10, 80), height=30),
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
