import os
from flask import flash, Flask, request, render_template

app = Flask(__name__)

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

        file.save(os.path.join('./upload', file.filename))
        return render_template('index.html', number=123456789)


if __name__ == '__main__':
    # Enable the debug mode, which restarts the server while saving
    app.debug = True

    app.secret_key = "I am the Key"
    app.run()
