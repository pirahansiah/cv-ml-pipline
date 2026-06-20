"""Image conversion utilities for FastAPI CV service."""

from __future__ import annotations

import base64

import cv2
import numpy as np


def change_numpy_image_to_base64(img: np.ndarray) -> str:
    _, buffer = cv2.imencode(".jpg", img)
    return base64.b64encode(buffer).decode()


def change_base64_to_numpy_image(b64_str: str) -> np.ndarray:
    b64_bytes = base64.b64decode(b64_str)
    np_data = np.frombuffer(b64_bytes, np.uint8)
    return cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)


def color_change(b64_input: str) -> str:
    """Convert a base64-encoded image from BGR to HSV color space and return as base64."""
    img = change_base64_to_numpy_image(b64_input)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return change_numpy_image_to_base64(hsv)
