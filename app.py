from flask import Flask, render_template, url_for, request, redirect, flash
from image_proc import *
import os
from werkzeug.utils import secure_filename
import cv2

app = Flask(__name__)

app.secret_key = "secret key"
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower()\
           in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        if request.method == 'POST':
            hex_code = request.form['hex']
            print(hex_code)
            image = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        hex_pixels = count_hex_pixels(img, hex_code)
        bl_or_wh = black_or_white(img)
        flash('Image successfully uploaded and displayed below')
        return render_template('index.html', filename=filename,
                               hex_pixels=hex_pixels, bl_or_wh=bl_or_wh)
    else:
        flash('Allowed image types are - png, jpg, jpeg')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == '__main__':
    app.run(debug=False)
