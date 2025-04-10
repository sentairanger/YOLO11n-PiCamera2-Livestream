from ultralytics import YOLO
from datetime import datetime
import cv2
import matplotlib.pyplot as plt
import matplotlib
import os

image_name = "image.jpg"
timestamp = int(datetime.timestamp(datetime.now())) 

matplotlib.use("Agg")

def prediction(model_type, img_path, display_result = False, task : str = None):

    model = YOLO(model_type)
    result = model(img_path, save = True, conf=0.5)

    for r in result:
        pred_img_path = f"{r.save_dir}/{img_path}"
        pred = cv2.cvtColor(cv2.imread(pred_img_path), cv2.COLOR_BGR2RGB)
        plt.imshow(pred)
        plt.axis('off')
        plt.title(f"YOLO11 - {task}")
    plt.savefig("static/gallery/image_detect_%s.jpg" % timestamp)

    if display_result:
       print(result)



# Load the pre-trained YOLOv11-Medium model
model_type = "yolo11n.pt"
img_path = image_name

