# model_dispatcher.py
# to choose which model to train

from sklearn import linear_model
from sklearn import ensemble
from sklearn import tree
from sklearn.svm import SVC

models = {
    'logistic_regression': linear_model.LogisticRegression(
        penalty='l2',
        C = 0.01,
        solver='liblinear',
        class_weight={0:0.6,1:0.5}
    ),
    
    'decision_tree': tree.DecisionTreeClassifier(
        criterion='gini',
        max_depth=3,
        max_features=0.6,
    ),

    'random_forest': ensemble.RandomForestClassifier(
        n_estimators=100,
        criterion='gini',
        max_depth=3,
        max_features=0.7,
        n_jobs = 4,
    ),

    'gradient_boosting': ensemble.GradientBoostingClassifier(
        n_estimators=50,
        learning_rate=0.01,
        max_depth=4,
        max_features=0.6,
    ),

}