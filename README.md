# MultiClassClassification
This is multi class classification model to predict music taste of person based on age and gender.
Here, the salary.csv file is the original data we have. It contains age, gender, taste fields. In that age, gender are independent variables (inputs) and taste is dependent variable (output). This data can be classified in three main category for male as a) fast_music b) medium_music c) slow_music. And for female it can be classified in a) fast_music_with_dance b) medium_music_with_walk c) slow_music_with_sleep. Inside code we used pandas, sklearn libraries. First loaded csv data in data frame with pandas library, then we devided data in train and test data sets with 0.2 percent of test data, means we will feed 0.8 percent data for learning into model and with remaining 0.2 percent test data we will make test to check accuracy of model. You can srote and load model locally as well if you don't want to create model every time with help of joblib, the commented code showing that part. In the last we predicted music taste for age of 31 female.

Below is sample output for prediction:

Model Accuracy: 0.75

Music taste prediction for age of 31 female:-------['slow_music_with_sleep']
