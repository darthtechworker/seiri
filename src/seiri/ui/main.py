from seiri.ui.components.options import build_options_box
from seiri.ui.components.preview import build_preview_box


def build_ui(app):
    """
    Build the UI.
    """

    build_options_box(app)
    build_preview_box(app)

    app.main_box.add(app.options_box)
    app.main_box.add(app.preview_box)

    init_ui(app)


def init_ui(app):
    """
    Initialize the UI.
    """
