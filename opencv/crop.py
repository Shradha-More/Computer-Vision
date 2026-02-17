import os
import cv2

img = cv2.imread('dogs.jpg')
print(img.shape)

cropped_img = img[30:80, 40:90]

cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)