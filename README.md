# IPL-WinProbability-Prediction
This is my machine learning project. In this project I have used IPL dataset of year 2008 - 2021 from Kaggle.com to train models for predicting the winning probability of teams in an IPL match. This project is an end-to-end application, I have created a chrome extension to display live winning probability of teams using the model trained on the IPL dataset. I have applied Plat and Isotonic calibration on the model's probability values to calibrate them and make them more reliable.

I have trained two models, one for first inning of the match and another for second inning of the match to get more accurate and realistic predictions.

## Table of Content
- [Data Preparation Inning-1](#dataprep1)
- [Data Preparation Inning-2](/Data%20Prep%20%26%20Model%20Building/notebooks/data_prep_inn-2.ipynb)
- [Randomised Match ID based splitting](/Data%20Prep%20%26%20Model%20Building/scripts/data_splitter.py)
- [Model Training Script](/Data%20Prep%20%26%20Model%20Building/scripts/training.py)
- [Model Evaluation](/Data%20Prep%20%26%20Model%20Building/notebooks/model_evaluation.ipynb)
- [Plat and Isotonic Calibration](/Data%20Prep%20%26%20Model%20Building/notebooks/Calibration.ipynb)
- [Flask API](/API/main.py)
- [Data Scraping](/API/beautifulSoup.py)
- [Pipeline](/API/functional.py)
- [Chrome Extension](/chrome-ext/)

<a name='dataprep1'>
<h2>Data Preparation Inning-1</h2>
</a>
[Notebook](/Data%20Prep%20%26%20Model%20Building/notebooks/data_prep_inn-1.ipynb)

