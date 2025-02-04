import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")

def draw_person_segmentation(img):

    image = cv2.resize(img, (256, 256))


    results = model(image)
    for result in results:
        for i, mask in enumerate(result.masks.xy):
            if int(result.boxes.cls[i]) == 0:
                polygon = np.array(mask, np.int32)
                cv2.fillPoly(image, [polygon], color=(0, 0, 0))
    return image,img

if __name__=='__main__':
    
    image_path = 'images/blurrr/ABHAY_2.jpeg'
    image, image_og = draw_person_segmentation(image_path)