"""Top-level package for gradioUploader."""

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
]

__author__ = """none"""
__email__ = "none"
__version__ = "0.0.1"

from .src.gradioUploader.nodes import NODE_CLASS_MAPPINGS
from .src.gradioUploader.nodes import NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./web"
