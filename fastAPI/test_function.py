"""Local function test: apply color_change without hitting the server."""

from __future__ import annotations

import base64
import sys

import cv2
import numpy as np

from farshid import color_change


def numpy_to_base64(img: np.ndarray) -> str:
    _, buf = cv2.imencode(".jpg", img)
    return base64.b64encode(buf).decode()


def base64_to_numpy(b64_str: str) -> np.ndarray:
    data = base64.b64decode(b64_str)
    return cv2.imdecode(np.frombuffer(data, np.uint8), cv2.IMREAD_UNCHANGED)


def main(image_path: str) -> None:
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: cannot read {image_path}", file=sys.stderr)
        sys.exit(1)

    b64 = numpy_to_base64(img)
    result_b64 = color_change(b64)
    out = base64_to_numpy(result_b64)
    cv2.imshow("output", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "a.jpg"
    main(path)
