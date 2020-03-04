import os
import cv2
import sys
import time
import glob
import numpy as np
import base64
import json
from PIL import Image
from io import StringIO
import argparse
import requests
from farshid import color_change


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


# start
img = cv2.imread('a.jpg')
img_process = change_numpy_image_to_base64(img)
# server
url = "http://localhost:8080/process"
payload = {'data': img_process}
res = requests.post(url, json=payload)
img_function = res.json()['image']
# print(img_function)
# # output
img_out = change_base64_to_numpy_image(img_function)
cv2.imshow('output ', img_out)
cv2.waitKey()
