"""Basic OpenCV thresholding demo — reads an image, applies Otsu's method, and displays results."""

from __future__ import annotations

import cv2
import numpy as np
from pathlib import Path


def load_image(path: Path) -> np.ndarray:
    img = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if img is None:
        raise FileNotFoundError(f"Cannot read image: {path}")
    return img


def to_grayscale(img: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def apply_otsu_threshold(gray: np.ndarray) -> np.ndarray:
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary


def main() -> None:
    img_path = Path(__file__).parent / "a.png"
    img = load_image(img_path)

    gray = to_grayscale(img)
    binary = apply_otsu_threshold(gray)

    cv2.imshow("original", img)
    cv2.imshow("otsu", binary)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
