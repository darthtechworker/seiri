# filepath: /Users/gauravpandey/Documents/vscode/seiri/src/seiri/ui/components/preview.py
import os
import platform

import toga
from toga.style.pack import BOLD, COLUMN, Pack

from seiri.utils.create_pdf import create_pdf
from seiri.utils.file import get_supported_images
from seiri.utils.preview_pdf import convert_pdf_to_images

PREVIEW_BUTTON_LABEL = "Update Preview"
PLACEHOLDER_IMAGE_PATH = None

if platform.system() == "Darwin":
    PLACEHOLDER_IMAGE_PATH = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../resources/preview.png")
    )


def build_preview_button(app):
    """
    Build the select output directory button.
    """

    app.preview_button = toga.Button(
        PREVIEW_BUTTON_LABEL,
        on_press=lambda widget: on_click_preview_button(widget, app),
        style=Pack(font_weight=BOLD, padding=(20, 275, 0, 275), height=30),
    )

    return app.preview_button


def on_click_preview_button(widget, app):
    """
    Handle the click event on the preview button.
    """

    create_pdf(app)
    convert_pdf_to_images(app)

    app.images = get_supported_images(app.working_directory)

    if app.images:
        app.preview_image.image = toga.Image(
            os.path.join(app.working_directory, app.images[0])
        )
        app.image_slider.min = 0
        app.image_slider.max = len(app.images) - 1
        app.image_slider.value = 0


def build_preview_image(app):
    """
    Build the preview image.
    """

    app.preview_image = toga.ImageView(
        image=toga.Image(PLACEHOLDER_IMAGE_PATH),
        style=Pack(flex=1, padding=20, alignment="center"),
    )

    return app.preview_image


def build_image_slider(app):
    """
    Build the image slider.
    """

    app.image_slider = toga.Slider(
        min=0,
        max=0,
        on_change=lambda widget: on_slider_change(widget, app),
        style=Pack(flex=1, padding=20),
    )

    return app.image_slider


def on_slider_change(widget, app):
    """
    Handle the slider change event.
    """

    if app.images:
        index = int(widget.value)
        app.preview_image.image = toga.Image(
            os.path.join(app.working_directory, app.images[index])
        )


def build_preview_box(app):
    """
    Build the preview box.
    """

    build_preview_button(app)
    build_preview_image(app)
    build_image_slider(app)

    app.preview_box = toga.Box(style=Pack(direction=COLUMN, flex=2))
    app.preview_box.add(app.preview_button)
    app.preview_box.add(app.preview_image)
    app.preview_box.add(app.image_slider)

    return app.preview_box
