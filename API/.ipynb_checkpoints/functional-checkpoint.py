import pandas as pd
import numpy as np
import pickle
from warnings import filterwarnings
filterwarnings("ignore")

# test = {'inning':2,
#         'current_over': {70512: 18},
#  'current_ball_of_over': {70512: 6},
#  'total_extra_runs': {70512: 7},
#  'current_score': {70512: 119},
#  'wicket_loss': {70512: 10},
#  'fours_team2': {70512: 11},
#  'sixes_team2': {70512: 3},
#  'balls_left': {70512: 6},
#  'current_run_rate': {70512: 6.263157894736842},
#  'over_left': {70512: 1},
#  'team1_score': {70512: 139},
#  'team1_wickets': {70512: 7},
#  'team1_extra_runs': {70512: 12},
#  'over_playedBy_team1': {70512: 20},
#  'team1': {70512: 'Punjab Kings'},
#  'team2': {70512: 'Royal Challengers Bangalore'},
#  'required_runs': {70512: 20},
#  'required_run_rate': {70512: 20.0},
#  'venue': {70512: 'M Chinnaswamy Stadium'},
#  'team2_won_toss': {70512: 1}}

def model1(inps):
    with open("saved_pickle/encoders.pkl", "rb") as a:
        encoders = pickle.load(a)
    with open("saved_pickle/col_seq.pkl","rb") as b:
        col_seq = pickle.load(b)
    encoder = encoders['encoder']
    min_scaler = encoders['min_scaler']
    with open("saved_pickle/model_inn_new.pkl","rb") as c:
        model = pickle.load(c)
    df = pd.DataFrame(inps, index=[0])
    df.drop('inning', axis=1, inplace=True)
    df = df[col_seq]
    # df.drop('inn', axis=1,inplace=True)
    X_test = df
    
    numerical_cols = min_scaler.transform(X_test.select_dtypes(exclude='object'))
    categorical_cols = encoder.transform(X_test.select_dtypes(include='object'))

    X_test = np.hstack((numerical_cols,categorical_cols))
    # X_test = X_test.reindex(columns = col_seq, fill_value=0)  
    # X_test = X_test.drop(columns='id')
    # X_test = scaler.transform(X_test)
    prediction = model.predict_proba(X_test)
    return prediction   

def model2(inps):
    with open("saved_pickle/encoders2.pkl", "rb") as a:
        encoders = pickle.load(a)
    with open("saved_pickle/col_seq2.pkl","rb") as b:
        col_seq = pickle.load(b)   
        
    encoder = encoders['encoder']
    std_scaler = encoders['std_scaler']
    with open("saved_pickle/model_inn2.pkl","rb") as c:
        model = pickle.load(c)
    df = pd.DataFrame(inps, index = [0])
    
    df.drop('inning', axis=1, inplace=True)
    df = df[col_seq]
    # df.drop('inn', axis=1,inplace=True)
    X_test = df
    
    numerical_cols = std_scaler.transform(X_test.select_dtypes(exclude='object'))
    categorical_cols = encoder.transform(X_test.select_dtypes(include='object'))

    X_test = np.hstack((numerical_cols,categorical_cols))
    # X_test = X_test.reindex(columns = col_seq, fill_value=0)  
    # X_test = X_test.drop(columns='id')
    # X_test = scaler.transform(X_test)
    prediction = model.predict_proba(X_test)
    win = model.predict(X_test)
    return prediction
        
# model2(test)
        