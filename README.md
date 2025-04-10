# YOLO11n-PiCamera2-Livestream
This project uses Ultralytics for Object Detection, Pi Camera for the Video Feed and Flask to serve the Web UI

## Getting Started

This has been tested on a Pi 4, but will work on a Pi 5, CM4 and CM5. You can use any Pi Camera Module you want. To get started you will need a virtual environment. If you want to use the system wide libraries use this command: `python3 -m venv --system-site-packages torchenv`. The `torchenv` is a name you can use for your environment. Next, activate with `source torchenv/bin/activate`. Install the needed libraries like `pytorch` and `ultralytics`. Also make sure you install the other libraries that will be requried. Run the code with `python3 app.py`. You can then take pictures, perform inference on the picture and check out your gallery. Screenshot posted below.

![https://github.com/sentairanger/YOLO11n-PiCamera2-Livestream/blob/main/app.png](app)
