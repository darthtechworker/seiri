# filepath: /Users/gauravpandey/Documents/vscode/seiri/src/seiri/ui/components/preview.py
import toga
from toga.style.pack import BOLD, COLUMN, Pack

from seiri.create_pdf import create_pdf

PREVIEW_BUTTON_LABEL = "Preview"


def build_preview_button(app):
    """
    Build the select output directory button.
    """

    app.preview_button = toga.Button(
        PREVIEW_BUTTON_LABEL,
        on_press=lambda widget: on_click_preview_button(widget, app),
        style=Pack(font_weight=BOLD, padding=(20, 275, 10, 275), height=30),
    )

    return app.preview_button


def on_click_preview_button(widget, app):
    """
    Handle the click event on the preview button.
    """

    create_pdf(app)


def build_preview_box(app):
    """
    Build the preview box.
    """

    build_preview_button(app)

    app.preview_box = toga.Box(style=Pack(direction=COLUMN, flex=2))
    app.preview_box.add(app.preview_button)

    return app.preview_box
