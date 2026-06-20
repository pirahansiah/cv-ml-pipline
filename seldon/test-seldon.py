"""Send a test image to Seldon Core for grayscale conversion."""

from __future__ import annotations

import sys

import cv2
import numpy as np
import requests


def test_seldon(image_path: str, url: str = "http://localhost:5000/predict") -> None:
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: cannot read {image_path}", file=sys.stderr)
        sys.exit(1)

    payload = {
        "data": {"tensor": {"shape": list(img.shape), "values": img.reshape(-1).tolist()}}
    }
    resp = requests.post(url, json=payload, timeout=10)
    resp.raise_for_status()

    data = resp.json()["data"]
    shape = data["tensor"]["shape"]
    output = np.array(data["tensor"]["values"], dtype=np.uint8).reshape(shape[1], shape[2])
    cv2.imshow("seldon output", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "a.jpg"
    test_seldon(path)
