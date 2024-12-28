## general importings
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import io
import base64
from werkzeug.utils import secure_filename

## loading data
from packages.load_dataset import read_csv_file, read_excel_file, file_shape, categorical_columns, numerical_columns, boolean_colums, head

## importing evaluation models
from packages.evaluate_models import evaluate_classification_model, evaluate_regression_model



app = Flask(__name__)

## routing the home page
@app.route('/')
def home():
    return render_template('home.html')
## routing the data inspection page
@app.route('/data-inspection', methods=['GET','POST'])
def data_inspection():
    if request.method == 'POST':
        file = request.files.get('files')

        if file:
            if file.filename.endswith('.csv'):
                df = pd.read_csv(io.BytesIO(file.read()))
            elif file.filename.endswith('.xlsx'):
                df = pd.read_excel(io.BytesIO(file.read()))
            else:
                return 'Invalid file type. Please upload a CSV or XLSX file.'

            # Calculate rows and columns
            rows, cols = df.shape

            return render_template('data_inspection.html', columns=cols, rows=rows, column_names = df.columns)

    ## Render the form for GET requests or if no file is uploaded
    return render_template('data_inspection.html', columns=None, rows=None)
    


## routing the data visulizaion page
@app.route('/data-visualization')
def data_visualization():
    return render_template('data_visualization.html')

@app.route('/model-selection')
def model_selection():
    return render_template('model_selection.html')

@app.route('/model-evaluation')
def model_evaluation():
    return render_template('model_eval.html')

@app.route('/model-prediction')
def model_prediction():
    return render_template('model_prediction.html')

if __name__=='__main__':
    app.run(debug=True)
