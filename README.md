# IPL-WinProbability-Prediction
This is my machine learning project. In this project I have used IPL dataset of year 2008 - 2021 from Kaggle.com to train models for predicting the winning probability of teams in an IPL match. This project is an end-to-end application, I have created a chrome extension to display live winning probability of teams using the model trained on the IPL dataset. I have applied Plat and Isotonic calibration on the model's probability values to calibrate them and make them more reliable.

I have trained two models, one for first inning of the match and another for second inning of the match to get more accurate and realistic predictions.

## Table of Content
- [Data Preparation Inning-1](#dataprep1)
- [Data Preparation Inning-2](#dataprep2)
- [Randomised Match ID based splitting](#datasplit)
- [Model Training Script](#training)
- [Model Evaluation](#evaluate)
- [Plat and Isotonic Calibration](#calibration)
- [Flask API](/API/main.py)
- [Data Scraping](/API/beautifulSoup.py)
- [Pipeline](/API/functional.py)
- [Chrome Extension](/chrome-ext/)

<a name='dataprep1'>
<h2>Data Preparation Inning-1</h2>
</a>

Data preparation using inning-1 data, for this I used **`pandas`** library to explore the data and create new features from the existing features. The notebook given below is the notebook for preparing data for inning-1.

[Notebook](/Data%20Prep%20%26%20Model%20Building/notebooks/data_prep_inn-1.ipynb)

<a name='dataprep2'>
<h2>Data Preparation Inning-2</h2>
</a>

Data preparation using inning-2 data, for this I used **`pandas`** library to explore the data and create new features from the existing features. The notebook given below is the notebook for preparing data for inning-2.

[Notebook](/Data%20Prep%20%26%20Model%20Building/notebooks/data_prep_inn-2.ipynb)

<a name='datasplit'>
<h2>Randomised Match ID based splitting</h2>
</a>

For splitting my data for model training I did not use the standard **`train_test_split`** from **`sklearn`** library because using the standard train-test split there was great chance of **data leakage** and hence model trained using that data was highly overfit. Hence, I split the data manually by shuffling the match IDs. This lowers the risk of data leakage. Given below is the python script for the same.

[Script](/Data%20Prep%20%26%20Model%20Building/scripts/data_splitter.py)

<a name='training'>
<h2>Model Training Script</h2>
</a>

Once, we have split our data. We are ready to train our model. For this project I trained different ML models like, `Logistic Regression`, `Decision Tree`, `Random Forest`, and `Gradient Boosting Decision Tree`. For this purpose, instead of writing the codes in one notebook, I created a python script to automate the process of training different models and saving them instantly using command line prompt with the help of command line arguments. All you need to do is, run this python script from command prompt and pass arguments like `path` of the data, `inn` which is inning of the match, `model_num` which is the number of model we are currently training (this is for saving the model automatically after each run of the script), and finally the `model` the name of the model we want to train (this is recognised by another script, which is **`model_dispatcher`**, it consists of the mapping of model name to its model). The script given below is the script for the automated training of models.

[Script]((/Data%20Prep%20%26%20Model%20Building/scripts/training.py)

<a name='evaluate'>
<h2>Model Evaluation</h2>
</a>

In this notebook, I have the code for evaluating each model's performance trained and saved using the `training.py` script. The code consists of different evaluation metrics such as `Confusion Matrix`, `Precision Recall Curve`, `Receiver Operating Curve` and **a special plot to show the trend of accuracy with delivery of each over in the match** which gives a realistic performance evaluation for this particular application. See the notebook below.

[Notebook](/Data%20Prep%20%26%20Model%20Building/notebooks/model_evaluation.ipynb)

<a name='calibration'>
<h2>Plat and Isotonic Calibration</h2>
</a>

This is the very important task in the whole project. Since, our application relies on the probablities (We are predicting the probablity of win for the teams) it is very necessary to apply **calibration** on the probabilities given by our trained models. The probability needs to be more confident for our binary classification, if the class of a sample is positive then the probability of saying its positive should be high (more confident) so that we can rely upon that probability. The probabilites given by the models are not reliable, they are very less confident and hence there is need for **calibration** of the probabilities. See the image below to understand why calibration is important.

### Density Plot
The image shown below, shows the distribution of probabilities given by the model for trai and test data respectively. As we can see the densities at the ends (0 and 1) are not so high. Which means the model is less confident with the classification.

![](/images/calibration1.png)

The curve shown in the image below is called **reliability curve**. The dotted line in the plot is the ideal behaviour for the model we expect and the blue curve is the result of our model which is not at all reliable. Hence we need to calibrate the probabilites. Calibration of probabilities will bring the curve close to the expected behavior.

![](/images/calibration2.png)

### Isotonic and Plat Calibration
The plot shown below is the **reliablity curve** after we calibrate the probabilites. The green curve is for the **Isotonic Calibration** and the orange curve is for **Plat Calibration**. As we can see the Isotonic Calibrated probabilities give us more close to ideal behavior of the model we choose that for our final probabilities on which we can rely on.

![](/images/calibration4.png)

### Density plot after calibration
Shown below is the density plot after calibration. We can see the density at the edges (0 and 1) is much high compared to the previous plot, which means we can rely more on these probabilites rather than the old ones as they are more confident.

![](/images/calibration5.png)