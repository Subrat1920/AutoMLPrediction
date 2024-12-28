from flask import Flask, request, flash, url_for, redirect
from werkzeug.utils import secure_filename
import os
def allowed_file(filename):
    ## check if the file has an allowed extension
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def upload_folder():
    if 'files' not in request.files:
        flash("No files part in the request")
        return redirect(url_for('data_inspection'))
    
    uploaded_files = request.files.getlist('files')
    for file in uploaded_files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
