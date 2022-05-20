# IPL-WinProbability-Prediction
This is my ML project which is to predict the live winning probabilities of teams in IPL match

Objective: 
The aim of the project is to predict live winning probabilities for teams and show the results in a browser extension.

Methodology: 
We took the IPL 2008-2020 dataset from Kaggle and prepared two separate datasets for Inning 1 and Inning 2, for training two different models for different innings.
In data preparation step we used the given features in the data to create new features.
Then we trained different models using different Train Test split techniques like,1st. Standard train test split using sklearn's train_test_split method, 2nd. We split the data using the match IDs by randomly shuffling them and 3rd. We did time based (Temporal Splitting) splitting.
Then we trained different models like, Logistic Regression, Decision Tree, Random Forest Classifier and Gradient Boosting Classifier using each of the splitting techniques.
Gradient Boosting Classifier with Match IDs split technique performed the best compared to other models.
Then we created a brower extension to show the prediction results.
We created an API to GET and POST data from cricbuzz.com website using BeautifulSoup library to extract the match data from website and send it to the model in server to calculate probabilities for each teams.

Conclusion: 
Model for inning 1st is performing fairly well but its not that accurate, on the other hand the Model trained using 2nd inning data is performing better than model for inning 1 but yet the accuracy is not very good. 

Future Work: 
Model trained using Time Based splitting technique could have performed much better as with the help of it, a model could learn the sequential information about the match too if we could train an LSTM model, but for that an API is needed to continuosly send and store data in server which is not yet available.
