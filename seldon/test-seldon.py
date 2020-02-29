from typing import Iterable
import numpy as np
import cv2
import requests
import json

# payload = {"data": {"tensor": {"shape": example_img.shape,
#                               "values": example_img.reshape(-1).tolist()}}}

# fa = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
fa = cv2.imread('a.jpg')
payload = {
    "data": {"tensor": {"shape": fa.shape, "values": fa.reshape(-1).tolist()}}}

response = requests.post('http://localhost:5000/predict', json=payload)
# far = response.content
# r_json = response.json()
# ticket = r_json['ndarray']
# print(ticket)
# res = requests.Response


data = response.json()['data']
shape_image = data["tensor"]["shape"]

bb_list = data["tensor"]["values"]
bb_list = np.array(bb_list, dtype=np.uint8).reshape(
    shape_image[1], shape_image[2])
cv2.imshow("farshid", bb_list)
cv2.waitKey()


# prediction_list = response.json()['data']['ndarray']
# prediction_list = far.json()['data']['ndarray']
# np.array(prediction_list[1], dtype=bool)
# "data":{"names"
#

# mask = np.array(r_json, dtype=np.uint8)
# print(mask)
# cv2.imshow("farshid", mask)
# cv2.waitKey(1000)
# print(response.content)
# img = img.astype('uint8')
