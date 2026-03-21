from ultralytics import YOLO

import cv2


model_path = './last.pt'

image_path = '"D:\Desktop\Shraddha\Computer Vision\image_segmentation_with_yolov8\data\images\val\11902836553_50cacd360a_z.jpg"'

img = cv2.imread(image_path)
H, W, _ = img.shape

model = YOLO(model_path)

results = model(img)

for result in results:
    for j, mask in enumerate(result.masks.data):

        mask = mask.numpy() * 255

        mask = cv2.resize(mask, (W, H))

        cv2.imwrite('./output.png', mask)