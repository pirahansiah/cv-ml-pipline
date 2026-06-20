"""Seldon Core model wrapper for grayscale conversion."""

from __future__ import annotations

from typing import Any

import cv2
import numpy as np


class Farshid:
    def predict(
        self,
        X: np.ndarray,
        features_names: list[str] | None = None,
        meta: dict[str, Any] | None = None,
    ) -> list[np.ndarray]:
        arr = np.array(X, dtype=np.uint8)
        gray = cv2.cvtColor(arr, cv2.COLOR_BGR2GRAY)
        return [gray]
