def get_font_scale_factor(app):
    """
    Get the font scale factor.

    Parameters:
    app (Seiri): The Seiri app.

    Returns:
    float: The font scale factor.
    """

    base_height = 1872
    base_width = 1404

    scale_factor = min(app.device_height / base_height, app.device_width / base_width)

    return scale_factor
