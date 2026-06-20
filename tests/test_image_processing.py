"""Tests for root test.py image processing functions."""

from __future__ import annotations

import cv2
import numpy as np
import pytest
from pathlib import Path

from test import load_image, to_grayscale, apply_otsu_threshold


@pytest.fixture
def sample_image() -> np.ndarray:
    img_path = Path(__file__).resolve().parent.parent / "a.png"
    if img_path.exists():
        return load_image(img_path)
    return np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)


@pytest.fixture
def synthetic_bgr() -> np.ndarray:
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    img[:50, :, :] = 200
    img[50:, :, :] = 50
    return img


def test_to_grayscale() -> None:
    img = np.random.randint(0, 255, (64, 64, 3), dtype=np.uint8)
    gray = to_grayscale(img)
    assert gray.ndim == 2
    assert gray.shape == (64, 64)
    assert gray.dtype == np.uint8


def test_apply_otsu_threshold(synthetic_bgr: np.ndarray) -> None:
    gray = to_grayscale(synthetic_bgr)
    binary = apply_otsu_threshold(gray)
    assert binary.ndim == 2
    assert binary.shape == gray.shape
    unique = np.unique(binary)
    assert set(unique).issubset({0, 255})


def test_otsu_returns_binary_image() -> None:
    gray = np.random.randint(0, 255, (50, 50), dtype=np.uint8)
    binary = apply_otsu_threshold(gray)
    assert binary.min() == 0
    assert binary.max() == 255


def test_load_image_missing() -> None:
    with pytest.raises(FileNotFoundError):
        load_image(Path("/nonexistent/path.png"))
