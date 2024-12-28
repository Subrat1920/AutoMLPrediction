import pandas as pd

## reading csv file
def read_csv_file(file_name):
    return pd.read_csv(file_name)

## reading excel file
def read_excel_file(file_name):
    return pd.read_excel(file_name)

## checking the shape, rows and columns of the dataset
def file_shape(data_frame):
    shape = data_frame.shape
    rows = shape[0]
    columns = shape[1]
    return  rows, columns

## head of the df
def head(data_frame, num_of_samples):
    return data_frame.head(num_of_samples)

## numerical column names
def numerical_columns(data_frame):
    result = [x for x in data_frame.columns if data_frame[x].dtypes in ['int64', 'float64', 'int32', 'float32', 'int', 'float']]
    return result

def categorical_columns(data_frame):
    result = [x for x in data_frame.columns if data_frame[x].dtypes in ['object']]
    return result

def boolean_colums(data_frame):
    result = [x for x in data_frame.columns if data_frame[x].columns in ['bool']]
    return result


