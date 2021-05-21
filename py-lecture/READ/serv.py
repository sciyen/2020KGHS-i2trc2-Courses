import os
from flask import flash, Flask, request, render_template, send_from_directory
import readImg
import classification

app = Flask(__name__, static_url_path='')

model = classification.load('./model/cnn_com.h5')


@app.route('/')
def root():
    '''
    Routing for root path, which renders the index.html page.
    '''
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    '''
    Routing for the upload request, which checks the file's validation
    and save the image to the 'upload' folder.
    '''
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('There is no file uploaded')
            return render_template('index.html', warning_msg='There is no file uploaded')

        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return render_template('index.html', warning_msg='No selected file')

        img_filename = os.path.join('./upload', file.filename)
        output_filename = os.path.join('./upload', 'out' + file.filename)
        file.save(img_filename)

        image = readImg.readImg(img_filename, output_filename)

        numbers = classification.predict(model, image)

        return render_template('index.html', number=numbers, img_path=output_filename)


@app.route('/upload/<path:path>')
def send_img(path):
    return send_from_directory('upload', path)


if __name__ == '__main__':
    # Enable the debug mode, which restarts the server while saving
    app.debug = True

    app.secret_key = "I am the Key"
    app.run(host="0.0.0.0", port=10418)
