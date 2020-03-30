import numpy as np
import cv2
#   X   Y

# 0/0---X--->
#  |
#  |
#  Y
#  |
#  |
#  v
#

#   Col   Row

# 0/0---column--->
#  |
#  |
# row
#  |
#  |
#  v

# start
img = cv2.imread('a.png')
# process
rows, cols = img.shape[:2]
frame = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # 0 .. 255
# for i in range(rows):
#     for j in range(cols):
#         if frame.item(i, j) > 130:
#             frame.itemset((i, j), 255)
#         else:
#             frame.itemset((i, j), 0)
# # output
img_out = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, img_out = cv2.threshold(img_out, 127, 255, cv2.THRESH_OTSU)

img_out = frame
cv2.imshow('original ', img)
cv2.imshow('output ', img_out)
cv2.waitKey()
