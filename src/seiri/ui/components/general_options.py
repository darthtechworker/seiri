import toga
from toga.style.pack import BOLD, COLUMN, ROW, Pack

DEVICE_HEIGHT_LABEL = "Device Height:"
DEVICE_WIDTH_LABEL = "Device Width:"
MARGIN_TOP_LABEL = "Margin Top:"
MARGIN_RIGHT_LABEL = "Margin Right:"
MARGIN_BOTTOM_LABEL = "Margin Bottom:"
MARGIN_LEFT_LABEL = "Margin Left:"


def build_device_height_container(app):
    """
    Build the device height container.
    """

    app.device_height_label = toga.Label(
        text=DEVICE_HEIGHT_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 34, 0, 0)),
    )
    app.device_height_input = toga.TextInput(
        style=Pack(width=67),
        placeholder="px",
        on_change=lambda widget: on_change_device_height_input(widget, app),
    )

    app.device_height_container = toga.Box(
        style=Pack(direction=ROW, padding=(0, 0, 10, 0))
    )
    app.device_height_container.add(app.device_height_label)
    app.device_height_container.add(app.device_height_input)


def on_change_device_height_input(widget, app):
    """
    Handle the change event on the device height input.
    """

    widget.on_change = None
    widget.value = "".join(filter(str.isdigit, widget.value))
    app.device_height = int(widget.value) if widget.value else None
    widget.on_change = lambda widget: on_change_device_height_input(widget, app)


def build_device_width_container(app):
    """
    Build the device width container.
    """

    app.device_width_label = toga.Label(
        text=DEVICE_WIDTH_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 39, 0, 0)),
    )
    app.device_width_input = toga.TextInput(
        style=Pack(width=67),
        placeholder="px",
        on_change=lambda widget: on_change_device_width_input(widget, app),
    )

    app.device_width_container = toga.Box(
        style=Pack(direction=ROW, padding=(0, 0, 10, 0))
    )
    app.device_width_container.add(app.device_width_label)
    app.device_width_container.add(app.device_width_input)


def on_change_device_width_input(widget, app):
    """
    Handle the change event on the device width input.
    """

    widget.on_change = None
    widget.value = "".join(filter(str.isdigit, widget.value))
    app.device_width = int(widget.value) if widget.value else None
    widget.on_change = lambda widget: on_change_device_width_input(widget, app)


def build_margin_top_container(app):
    """
    Build the margin top container.
    """

    app.margin_top_label = toga.Label(
        text=MARGIN_TOP_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 54, 0, 0)),
    )
    app.margin_top_input = toga.TextInput(
        style=Pack(width=67),
        placeholder="px",
        on_change=lambda widget: on_change_margin_top_input(widget, app),
    )

    app.margin_top_container = toga.Box(
        style=Pack(direction=ROW, padding=(0, 0, 10, 0))
    )
    app.margin_top_container.add(app.margin_top_label)
    app.margin_top_container.add(app.margin_top_input)


def on_change_margin_top_input(widget, app):
    """
    Handle the change event on the margin top input.
    """

    widget.on_change = None
    widget.value = "".join(filter(str.isdigit, widget.value))
    app.margin_top = int(widget.value) if widget.value else None
    widget.on_change = lambda widget: on_change_margin_top_input(widget, app)


def build_margin_right_container(app):
    """
    Build the margin right container.
    """

    app.margin_right_label = toga.Label(
        text=MARGIN_RIGHT_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 43, 0, 0)),
    )
    app.margin_right_input = toga.TextInput(
        style=Pack(width=67),
        placeholder="px",
        on_change=lambda widget: on_change_margin_right_input(widget, app),
    )

    app.margin_right_container = toga.Box(
        style=Pack(direction=ROW, padding=(0, 0, 10, 0))
    )
    app.margin_right_container.add(app.margin_right_label)
    app.margin_right_container.add(app.margin_right_input)


def on_change_margin_right_input(widget, app):
    """
    Handle the change event on the margin right input.
    """

    widget.on_change = None
    widget.value = "".join(filter(str.isdigit, widget.value))
    app.margin_right = int(widget.value) if widget.value else None
    widget.on_change = lambda widget: on_change_margin_right_input(widget, app)


def build_margin_bottom_container(app):
    """
    Build the margin bottom container.
    """

    app.margin_bottom_label = toga.Label(
        text=MARGIN_BOTTOM_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 30, 0, 0)),
    )
    app.margin_bottom_input = toga.TextInput(
        style=Pack(width=67),
        placeholder="px",
        on_change=lambda widget: on_change_margin_bottom_input(widget, app),
    )

    app.margin_bottom_container = toga.Box(
        style=Pack(direction=ROW, padding=(0, 0, 10, 0))
    )
    app.margin_bottom_container.add(app.margin_bottom_label)
    app.margin_bottom_container.add(app.margin_bottom_input)


def on_change_margin_bottom_input(widget, app):
    """
    Handle the change event on the margin bottom input.
    """

    widget.on_change = None
    widget.value = "".join(filter(str.isdigit, widget.value))
    app.margin_bottom = int(widget.value) if widget.value else None
    widget.on_change = lambda widget: on_change_margin_bottom_input(widget, app)


def build_margin_left_container(app):
    """
    Build the margin left container.
    """

    app.margin_left_label = toga.Label(
        text=MARGIN_LEFT_LABEL,
        style=Pack(font_weight=BOLD, padding=(0, 51, 0, 0)),
    )
    app.margin_left_input = toga.TextInput(
        style=Pack(width=67),
        placeholder="px",
        on_change=lambda widget: on_change_margin_left_input(widget, app),
    )

    app.margin_left_container = toga.Box(style=Pack(direction=ROW))
    app.margin_left_container.add(app.margin_left_label)
    app.margin_left_container.add(app.margin_left_input)


def on_change_margin_left_input(widget, app):
    """
    Handle the change event on the margin left input.
    """

    widget.on_change = None
    widget.value = "".join(filter(str.isdigit, widget.value))
    app.margin_left = int(widget.value) if widget.value else None
    widget.on_change = lambda widget: on_change_margin_left_input(widget, app)


def build_general_options_container(app):
    """
    Build the general options container.
    """

    build_device_height_container(app)
    build_device_width_container(app)
    build_margin_top_container(app)
    build_margin_right_container(app)
    build_margin_bottom_container(app)
    build_margin_left_container(app)

    app.general_options_container = toga.Box(
        style=Pack(direction=COLUMN, alignment="center", padding=(10, 0, 0, 0))
    )
    app.general_options_container.add(app.device_height_container)
    app.general_options_container.add(app.device_width_container)
    app.general_options_container.add(app.margin_top_container)
    app.general_options_container.add(app.margin_right_container)
    app.general_options_container.add(app.margin_bottom_container)
    app.general_options_container.add(app.margin_left_container)

    return app.general_options_container
