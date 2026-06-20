"""Tests for FastAPI image conversion utilities."""

from __future__ import annotations

import base64

import cv2
import numpy as np
import pytest

from fastAPI.farshid import (
    change_numpy_image_to_base64,
    change_base64_to_numpy_image,
    color_change,
)


@pytest.fixture
def sample_b64() -> str:
    img = np.random.randint(0, 255, (64, 64, 3), dtype=np.uint8)
    return change_numpy_image_to_base64(img)


def test_numpy_to_base64_roundtrip() -> None:
    img = np.random.randint(0, 255, (32, 32, 3), dtype=np.uint8)
    b64 = change_numpy_image_to_base64(img)
    assert isinstance(b64, str)
    decoded = base64.b64decode(b64)
    assert len(decoded) > 0


def test_base64_to_numpy_roundtrip() -> None:
    img = np.random.randint(0, 255, (32, 32, 3), dtype=np.uint8)
    b64 = change_numpy_image_to_base64(img)
    recovered = change_base64_to_numpy_image(b64)
    assert recovered is not None
    assert recovered.ndim == 3


def test_color_change_returns_b64(sample_b64: str) -> None:
    result = color_change(sample_b64)
    assert isinstance(result, str)
    decoded = base64.b64decode(result)
    assert len(decoded) > 0


def test_color_change_hsv_conversion() -> None:
    img = np.zeros((10, 10, 3), dtype=np.uint8)
    img[:, :, 0] = 100
    img[:, :, 1] = 200
    img[:, :, 2] = 150
    b64 = change_numpy_image_to_base64(img)
    result_b64 = color_change(b64)
    result_img = change_base64_to_numpy_image(result_b64)
    assert result_img is not None


def test_invalid_base64_raises() -> None:
    with pytest.raises(Exception):
        change_base64_to_numpy_image("not-valid-base64!!!")
