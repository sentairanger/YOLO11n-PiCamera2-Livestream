from flask import Flask, request, render_template, jsonify, Response, send_file
import os
import logging
from camera_setup import *
from time import sleep
from yolo_detect import *

app = Flask('__name__')

UPLOAD_FOLDER = 'static/gallery'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html", title="YOLO11n PiCamera2 Livestream UI")

@app.route("/gallery")
def gallery():
    try:
        image_files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith(('.jpg'))]
        if not image_files:
            return render_template("no_files.html")
        files = []
        for image_file in image_files:
            files.append({'filename' : image_file})
        return render_template("gallery.html", image_files=files)
    except Exception as ex:
        logging.error(f"Error in Finding Images: {ex}")
        return render_template("error.html")

@app.route("/dataimage")
def data_image():
    try:
        image_file = 'image.jpg'
        if os.path.exists(image_file):
            return render_template("data.html", image_url="/image_direct")
        else:
            return render_template("no_files.html")
    except Exception as ex:
        logging.error(f"Error in finding images: {ex}")
        return render_template("error.html")

@app.route("/image_direct")
def image_direct():
    return send_file("image.jpg", mimetype="image/jpeg")

@app.route("/capture", methods=['POST'])
def capture_photo():
    try:
        take_photo()
        sleep(1)
        return jsonify(success=True, message="Photo captured successfully")
    except Exception as ex:
        return jsonify(success=False, message=str(e))

@app.route("/yolo", methods=['POST'])
def yolo_detect():
    try:
        prediction(model_type, img_path, task = "Object Detection")
        return jsonify(success=True, message="Success")
    except Exception as ex:
        return jsonify(success=False, message=str(ex))

@app.route("/videofeed")
def videofeed():
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/delete_image/<filename>", methods=['DELETE'])
def delete_image(filename):
    try:
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        os.remove(filepath)
        return jsonify(success=True, message="Image deleted successfully")
    except Exception as ex:
        return jsonify(success=False, message=str(ex))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    start_stream()
    app.run(host='0.0.0.0')
