import os
# import magic
import urllib.request

import readarchive
from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
vet_file = []
ALLOWED_EXTENSIONS = set(['txt', 'doc'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the files part
        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)
        files = request.files.getlist('files[]')
        for file in files:
            if file and allowed_file(file.filename):
                vet_file.append(file.filename)
        readarchive.inicia(vet_file)
        flash('File(s) successfully uploaded')
        return redirect('/')


if __name__ == "__main__":
    app.run()