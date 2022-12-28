import pandas as pd
import numpy as np
import pickle
from warnings import filterwarnings
filterwarnings("ignore")

# for testing purpose

# test = {
#     'inning':2,
#     'current_over': {70512: 18},
#     'current_ball_of_over': {70512: 6},
#     'total_extra_runs': {70512: 7},
#     'current_score': {70512: 119},
#     'wicket_loss': {70512: 10},
#     'fours_team2': {70512: 11},
#     'sixes_team2': {70512: 3},
#     'balls_left': {70512: 6},
#     'current_run_rate': {70512: 6.263157894736842},
#     'over_left': {70512: 1},
#     'team1_score': {70512: 139},
#     'team1_wickets': {70512: 7},
#     'team1_extra_runs': {70512: 12},
#     'over_playedBy_team1': {70512: 20},
#     'team1': {70512: 'Punjab Kings'},
#     'team2': {70512: 'Royal Challengers Bangalore'},
#     'required_runs': {70512: 20},
#     'required_run_rate': {70512: 20.0},
#     'venue': {70512: 'M Chinnaswamy Stadium'},
#     'team2_won_toss': {70512: 1}
# }

def model1(inps):
    # getting data
    with open("data/data_inn1_model4.pkl", "rb") as f:
        data = pickle.load(f)
    
    # getting calibrator
    with open("calibrator/model1_logres_cal.pkl", "rb") as f:
        calibrator = pickle.load(f)
        
    # getting column sequence
    with open("data/col_seq.pkl", "rb") as f:
        col_seq = pickle.load(f)
        
    # getting encoder
    encoder = data['encoder']
    
    # getting scaler
    min_scaler = data['min_scaler']
    
    # converting data dictionary into
    # a dataframe
    df = pd.DataFrame(inps)
    df.drop('inning', axis=1, inplace=True)
    df = df[col_seq]
    
    numerical_cols = min_scaler.transform(
        df.select_dtypes(exclude='object')
    )
    
    categorical_cols = encoder.transform(
        df.select_dtypes(include='object')
    )

    X_test = np.hstack((numerical_cols,categorical_cols))
    
    # applying isotonic calibration
    cal = calibrator['iso']
    
    # getting calibrated probability
    true_proba = cal.predict_proba(X_test)
    
    return true_proba

def model2(inps):
    # getting data
    with open("data/data_inn2_model1.pkl", "rb") as f:
        data = pickle.load(f)

    # getting calibrator
    with open("calibrator/model2_gbdt_cal2.pkl", "rb") as f:
        calibrator = pickle.load(f)
        
    # getting column sequence
    with open("data/col_seq2.pkl", "rb") as f:
        col_seq = pickle.load(f)
        
    # getting encoder
    encoder = data['encoder']
    
    # getting scaler
    min_scaler = data['min_scaler']
        
    # converting data dictionary into
    # dataframe
    df = pd.DataFrame(inps)
    df.drop('inning', axis=1, inplace=True)
    df = df[col_seq]
    
    numerical_cols = min_scaler.transform(
        df.select_dtypes(exclude='object')
    )
    
    categorical_cols = encoder.transform(
        df.select_dtypes(include='object')
    )

    X_test = np.hstack((numerical_cols,categorical_cols))

    # applying isotonic calibration
    cal = calibrator['iso']
    
    # getting calibrated probability
    true_proba = cal.predict_proba(X_test)
    
    return true_proba
        
# model2(test)