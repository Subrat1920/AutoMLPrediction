from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, accuracy_score, precision_score, f1_score, recall_score, auc, roc_auc_score, roc_curve

## for classification model evaluation
def evaluate_classification_model(true, predicted):
    accuracy = accuracy_score(true, predicted)
    precision = precision_score(true, predicted)
    recall = recall_score(true, predicted)
    f1 = f1_score(true, predicted)
    return [accuracy, precision, recall, f1]

def evaluate_regression_model(true, predicted):
    mse = mean_squared_error(true, predicted)
    mae = mean_absolute_error(true, predicted)
    r2 = r2_score(true, predicted)
    return [mse, mae, r2]