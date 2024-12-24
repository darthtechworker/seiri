# filepath: /Users/gauravpandey/Documents/vscode/seiri/src/seiri/ui/components/preview.py
import os
import platform

import toga
from toga.style.pack import BOLD, COLUMN, Pack

from seiri.utils.create_pdf import create_pdf
from seiri.utils.preview_pdf import convert_pdf_to_images, get_number_of_pages

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

    number_of_pages = get_number_of_pages(app) - 1

    if number_of_pages:
        app.preview_image.image = toga.Image(convert_pdf_to_images(app, page_num=0))
        app.image_slider.min = 0
        app.image_slider.max = number_of_pages
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

    page_num = int(widget.value)
    app.preview_image.image = toga.Image(convert_pdf_to_images(app, page_num=page_num))


def build_preview_container(app):
    """
    Build the preview container.
    """

    build_preview_button(app)
    build_preview_image(app)
    build_image_slider(app)

    app.preview_container = toga.Box(style=Pack(direction=COLUMN, flex=2))
    app.preview_container.add(app.preview_button)
    app.preview_container.add(app.preview_image)
    app.preview_container.add(app.image_slider)

    return app.preview_container
