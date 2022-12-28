import argparse
import pickle

import numpy as np

from data_splitter import get_modelling_data
from scipy.stats import randint, uniform

from sklearn import metrics

import model_dispatcher
from warnings import filterwarnings

filterwarnings("ignore")

def train(path, model, inn, model_num):
    model_num = 0 if model_num is None else model_num
    data = get_modelling_data(path)
    X_train = data['X_train']
    X_val = data['X_val']
    X_test = data['X_test']
    y_train = data['y_train']
    y_val = data['y_val']
    y_test = data['y_test']
    min_scaler = data['min_scaler']
    std_scaler = data['std_scaler']
    encoder = data['encoder']
    
    # train scaled
    numerical_cols = std_scaler.transform(
        X_train.select_dtypes(exclude='object')
    )
    
    categorical_cols = encoder.transform(
    X_train.select_dtypes(include='object')
    )

    X_train_scaled = np.hstack(
        (numerical_cols,categorical_cols)
    )
    
    # val_scaled
    numerical_cols_ = std_scaler.transform(
        X_val.select_dtypes(exclude='object')
    )
    categorical_cols_ = encoder.transform(
        X_val.select_dtypes(include='object')
    )

    X_val_scaled = np.hstack(
        (numerical_cols_,categorical_cols_)
    )
    
    # test_scaled
    numerical_cols__ = std_scaler.transform(
        X_test.select_dtypes(exclude='object')
    )
    categorical_cols__ = encoder.transform(
        X_test.select_dtypes(include='object')
    )

    X_test_scaled = np.hstack(
        (numerical_cols__,categorical_cols__)
    )

    clf = model_dispatcher.models[model]
    clf.fit(X_train_scaled, y_train)

    train_predict = clf.predict(X_train_scaled)
    # test_predict = clf.predict(X_test_scaled)
    test_predict = clf.predict(X_val_scaled)

    print(f"Train Accuracy: {metrics.accuracy_score(y_train, train_predict)}")
    # print(f"Test Accuracy: {metrics.accuracy_score(y_test, test_predict)}")
    print(f"Test Accuracy: {metrics.accuracy_score(y_val, test_predict)}")
    # print(f"AUC Score: {metrics.roc_auc_score(y_test, test_predict)}")
    print(f"AUC Score: {metrics.roc_auc_score(y_val, test_predict)}")

    with open(f"../models/model_for_calibration/{model}_inn{inn}_model{model_num}.bin", 'wb') as f:
        pickle.dump(clf, f)

    with open(f"../data/calibrator_data/data_inn{inn}_model{model_num}.pkl", 'wb') as d:
        pickle.dump(data, d)


if __name__ == "__main__":
    #initialize ArgumentParser class
    
    parser = argparse.ArgumentParser()
    
    #add command line arguments
    parser.add_argument("--path", type=str)

    parser.add_argument("--inn", type=str)
    
    parser.add_argument("--model_num", type=str)
    
    parser.add_argument("--model", type=str)
    
    #read the arguments from command line
    args = parser.parse_args()
    
    train(
        path = args.path,
        inn = args.inn,
        model = args.model,
        model_num = args.model_num,
    )