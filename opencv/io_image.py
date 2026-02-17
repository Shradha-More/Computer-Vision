import os
import cv2

# read image
img = cv2.imread('bird.jpg')

if img is None:
    print("Image not loaded. Check file name or location.")
else:
    # write image
    cv2.imwrite('bird_out.jpg', img)

    # visualize image
    cv2.imshow('image', img)
    cv2.waitKey(10000)
    cv2.destroyAllWindows()
