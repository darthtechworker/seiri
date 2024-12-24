from seiri.ui.components.options import build_options_container
from seiri.ui.components.preview import build_preview_container


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
    app.margin_top_input.value = 25
    app.margin_right_input.value = 25
    app.margin_bottom_input.value = 25
    app.margin_left_input.value = 25

    app.preview_button.enabled = False
