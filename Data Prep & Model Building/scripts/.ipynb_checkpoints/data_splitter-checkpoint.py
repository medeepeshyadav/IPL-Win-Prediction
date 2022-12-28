from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, StandardScaler
import pandas as pd
import numpy as np
import pickle
from warnings import filterwarnings
filterwarnings("ignore")

def get_modelling_data(path):
    dataset = pd.read_csv(path)
    matches = dataset.id.unique()

    np.random.shuffle(matches)
    
    y = dataset["team2_won_match"]
    dataset.drop("team2_won_match", axis=1, inplace=True)

    X_train = dataset[
        dataset.id.isin(
            matches[:int(0.70*len(matches))]
        )].reset_index(drop=True)
    
    X_val = dataset[
        dataset.id.isin(
            matches[int(0.70*len(matches)):int(0.85*len(matches))]
        )].reset_index(drop=True)
    
    X_test = dataset[
        dataset.id.isin(
            matches[int(0.85*len(matches)):]
        )].reset_index(drop=True)
    
    y_train = (
        ((y[dataset.id.isin(
            matches[:int(0.70*len(matches))]
        )])==1).astype(int)
    ).values
    
    y_val = (
        ((y[dataset.id.isin(
            matches[int(0.70*len(matches)):int(0.85*len(matches))]
        )])==1).astype(int)
    ).values
    
    y_test = (
        ((y[dataset.id.isin(
            matches[int(0.85*len(matches)):]
        )])==1).astype(int)
    ).values

    X_train.drop("id", axis=1,inplace=True)
    X_val.drop("id", axis=1,inplace=True)
    X_test.drop("id", axis=1,inplace=True)

    categorical_cols = X_train.select_dtypes(include ='object').values
    numerical_cols = X_train.select_dtypes(exclude='object').values

    encoder = OneHotEncoder(sparse = False, handle_unknown='ignore')
    encoder.fit(categorical_cols)
    min_scaler = MinMaxScaler()
    min_scaler.fit(numerical_cols)
    std_scaler = StandardScaler()
    std_scaler.fit(numerical_cols)
    
    return {
            "min_scaler":min_scaler,
            "std_scaler":std_scaler,
            "encoder":encoder,
            "X_train": X_train,
            "y_train": y_train,
            "X_val": X_val,
            "y_val": y_val,
            "X_test":X_test,
            "y_test":y_test
        }