"""Tests for Seldon model wrapper."""

from __future__ import annotations

import cv2
import numpy as np
import pytest

from seldon.Farshid import Farshid


@pytest.fixture
def model() -> Farshid:
    return Farshid()


def test_predict_grayscale_output(model: Farshid) -> None:
    img = np.random.randint(0, 255, (64, 64, 3), dtype=np.uint8)
    result = model.predict(img)
    assert len(result) == 1
    assert result[0].ndim == 2


def test_predict_grayscale_dtype(model: Farshid) -> None:
    img = np.random.randint(0, 255, (32, 32, 3), dtype=np.uint8)
    result = model.predict(img)
    assert result[0].dtype == np.uint8


def test_predict_preserves_dimensions(model: Farshid) -> None:
    h, w = 120, 160
    img = np.random.randint(0, 255, (h, w, 3), dtype=np.uint8)
    result = model.predict(img)
    assert result[0].shape == (h, w)
