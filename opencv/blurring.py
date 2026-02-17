import os
import cv2

img = cv2.imread('dogs.jpg')

k_size = 7
img_blur = cv2.blur(img, (k_size, k_size))
img_guassian_blur = cv2.GaussianBlur(img, (k_size, k_size), 5)
img_median_blur = cv2.medianBlur(img, k_size)

cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_guassian_blur', img_guassian_blur)
cv2.imshow('img_median_blur', img_median_blur)
cv2.waitKey(0)