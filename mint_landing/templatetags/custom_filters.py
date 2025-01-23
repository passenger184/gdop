import os

from django import template

register = template.Library()


@register.filter
def split_string(value, delimiter=","):
    """Split a string by a delimiter."""
    if isinstance(value, str):
        return value.split(delimiter)
    return value


@register.filter
def file_icon(file_name):
    """
    Returns the appropriate HTML for the file type icon based on the file extension.
    """
    icon_map = {
        ".pdf": "bi bi-file-earmark-pdf-fill text-danger",
        ".doc": "bi bi-file-earmark-word-fill text-primary",
        ".docx": "bi bi-file-earmark-word-fill text-primary",
        ".ppt": "bi bi-file-earmark-slides-fill text-warning",
        ".pptx": "bi bi-file-earmark-slides-fill text-warning",
        ".xls": "bi bi-file-earmark-excel-fill text-success",
        ".xlsx": "bi bi-file-earmark-excel-fill text-success",
        ".jpg": "bi bi-file-earmark-image-fill text-warning",
        ".jpeg": "bi bi-file-earmark-image-fill text-warning",
        ".png": "bi bi-file-earmark-image-fill text-warning",
        ".txt": "bi bi-file-earmark-text-fill text-secondary",
        ".zip": "bi bi-file-earmark-zip-fill text-muted",
        ".rar": "bi bi-file-earmark-zip-fill text-muted",
        ".mp4": "bi bi-file-earmark-play-fill text-info",
        ".mp3": "bi bi-file-earmark-music-fill text-info",
        # Default icon
        "default": "bi bi-file-earmark text-muted",
    }

    # Get the file extension
    _, ext = os.path.splitext(file_name.lower())

    # Get the icon class for the file type or fallback to 'default'
    icon_class = icon_map.get(ext, icon_map["default"])

    # Return the HTML for the icon
    return f'<i class="{icon_class}" style="font-size: 2rem;"></i>'
