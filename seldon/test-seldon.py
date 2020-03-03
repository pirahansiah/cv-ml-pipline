from typing import Iterable
import numpy as np
import cv2
import requests
import json

fa = cv2.imread('a.jpg')
payload = {
    "data": {"tensor": {"shape": fa.shape, "values": fa.reshape(-1).tolist()}}}
response = requests.post('http://localhost:5000/predict', json=payload)

data = response.json()['data']
shape_image = data["tensor"]["shape"]
output_image = data["tensor"]["values"]
output_image = np.array(output_image, dtype=np.uint8).reshape(
    shape_image[1], shape_image[2])
cv2.imshow("farshid", output_image)
cv2.waitKey()
