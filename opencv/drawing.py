import os
import cv2

img = cv2.imread('whiteboard.jpg')

print(img.shape)

# line
cv2.line(img, (100, 150), (120, 150), (0, 255, 0), 3)

# rectangle
cv2.rectangle(img, (50, 90), (120, 200), (0, 0, 255), -1)

# circle
cv2.circle(img, (100, 250), 10, (255, 0, 0), 10)

# text
cv2.putText(img, 'Hey You!', (100, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)