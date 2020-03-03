import cv2
import base64
import numpy as np
from PIL import Image
from io import StringIO
from fastapi import FastAPI
from pydantic import BaseModel


def change_numpy_image_to_base64(img):
    _, buffer = cv2.imencode('.jpg', img)
    img_b64_bytes = base64.b64encode(buffer)
    img_b64_str = img_b64_bytes.decode()
    return img_b64_str


def change_base64_to_numpy_image(b64_str):
    b64_bytes = base64.b64decode(b64_str)
    np_data = np.frombuffer(b64_bytes, np.uint8)
    img = cv2.imdecode(np_data, cv2.IMREAD_UNCHANGED)
    return img


def color_change(based_64_input):
    img_org = change_base64_to_numpy_image(based_64_input)
    img_change = cv2.cvtColor(img_org, cv2.COLOR_BGR2HSV)
    img_out_str = change_numpy_image_to_base64(img_change)
    return img_out_str
