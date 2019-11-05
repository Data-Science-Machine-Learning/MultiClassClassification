# DESCRIPTION
# This is example of Decision Tree Classifier model for measuring likelihood of music preffered by person as per age and gender
# Inputs: Age, Gender
# Output: taste of music (prediction based on Inputs)

# PREDICT IN THIS ORDER OF INPUT
# sample - age, gender

# CODES FOR GENDER
# 0 = female
# 1 = male

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

#Machine learning example, classification problem
music_data = pd.read_csv('music.csv')
X = music_data.drop(columns=['taste'])
Y = music_data['taste']

model = DecisionTreeClassifier()
# model.fit(X,Y)
# predict = model.predict([ [21,1],[34,0] ])
# predict

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
model.fit(x_train, y_train) #training model
predict = model.predict(x_test) #predict with test value

score = accuracy_score(y_test, predict)
print("Model Accuracy: "+str(score))


#How to make persistence model, model dump one time
#music_data = pd.read_csv('music.csv')
#X = music_data.drop(columns=['taste'])
#Y = music_data['taste']

#model = DecisionTreeClassifier()
#model.fit(X,Y)

#joblib.dump(model,'mymusic-model.joblib')


#Predict from model loaded locally
model = joblib.load('mymusic-model.joblib')

predict = model.predict([ [31,0] ])
print('Music taste prediction for age of 31 female:-------'+str(predict))
