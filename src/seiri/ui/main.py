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
