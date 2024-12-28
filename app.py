## general importings
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

## loading data
from packages.load_datasets.load_dataset import read_csv_file, read_excel_file, shape, categorical_columns, numerical_columns, boolean_colums, head

## importing evaluation models
from packages.evaluation.evaluate_models import evaluate_classification_model, evaluate_regression_model



app = Flask(__name__)

## routing the home page
@app.route('/')
def home():
    return render_template('home.html')
## routing the data inspection page
@app.route('/data-inspection')
def data_inspection():
    return render_template('data_inspection.html')

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
