from pathlib import Path

from seiri.ui.components.options import build_options_container
from seiri.ui.components.preview import build_preview_container, on_click_preview_button


def build_ui(app):
    """
    Build the UI.
    """

    build_options_container(app)
    build_preview_container(app)

    app.main_box.add(app.options_container)
    app.main_box.add(app.preview_container)

    init_ui(app)


def init_ui(app):
    """
    Initialize the UI.
    """

    app.device_height_input.value = 1872
    app.device_width_input.value = 1404
    app.margin_top_input.value = 50
    app.margin_right_input.value = 50
    app.margin_bottom_input.value = 50
    app.margin_left_input.value = 50
    app.year_dropdown.value = app.year_dropdown.items[0].value

    app.preview_button.enabled = False

    # TODO: remove this when the app is ready
    app.output_directory = Path("/Users/gauravpandey/Desktop/Seiri")
    app.working_directory = app.output_directory / ".tmp"
    app.preview_button.enabled = True
    on_click_preview_button(None, app)
