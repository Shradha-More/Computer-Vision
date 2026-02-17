import os

import cv2
import numpy as np

img = cv2.imread('bear.jpg')

img_edge = cv2.Canny(img, 200, 300)

img_edge_d = cv2.dilate(img_edge, np.ones((5, 5), dtype = np.int8))

img_edge_e = cv2.erode(img_edge, np.ones((5, 5), dtype = np.int8))

cv2.imshow('img', img)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_d', img_edge_d)
cv2.imshow('img_edge_e', img_edge_e)
cv2.waitKey(0)
