


import pandas as pd
import numpy as np


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

"""Data Collection and Processing"""

#load data from csv file using pandas DataFrame
titanic=pd.read_csv('train.csv')
#printing data first 5 rows using head()
titanic.head()

# find no of rows and column using shape attribute
titanic.shape

#getting some information about the data using info()
titanic.info()

# check the number of each column in missing values using isnull().sum
titanic.isnull().sum()

"""Handling the missing values"""

# Drop the Cabin column from the dataframe most of the value is missing thats why we cant find means so we drop this column using drop()
#for row we mention  axis = 0 and column axis = 1
# we droping column and assign in titanic_data
titanic_data=titanic.drop(columns='Cabin', axis=1)

# replacing in missing value in age column with mean value using fillna() means not available
titanic_data['Age'].fillna(titanic_data['Age'].mean(),inplace=True)

#finding the mode value in "Embarked " column
print(titanic_data['Embarked'].mode())

print(titanic_data['Embarked'].mode()[0])

# replacing the missing values in mode values in "Embarked" column
titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0],inplace=True)

# check again the number of each column in missing values using isnull().sum
titanic_data.isnull().sum()

"""Data Analysis"""

# getting statistical data measure using describe()
titanic_data.describe()

# finding the no of people survived or not using value_counts()
titanic_data['Survived'].value_counts()
#here 0 means not survived and 1 means survived

titanic_data.replace({'Sex':{'male':0,'female':1}, 'Embarked':{'S':0,'C':1,'Q':2}},inplace=True)



titanic_data.head()

"""Seprating feature and Target"""

X=titanic_data.drop(columns=['PassengerId','Name','Ticket','Survived'],axis=1)
Y=titanic_data['Survived']

print(X)

print(Y)

"""Splitting the data into training data and test data"""

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=2)

print(X_train.shape,Y_train.shape,X_test.shape,Y_test.shape)

# make decision

model = DecisionTreeClassifier()
model.fit(X_train,Y_train)
# v=model.predict([[3,0,40,1,80,2,0]])
# print(model.predict([[2,1,40,1,40,2,1]]))
# print(Y)
# if v== 1:
#     print('survived')
# elif v== 0:
#     print('no')    
#     #creating file
    
import joblib
    
file='job_modell.sav'
joblib.dump(model,file)
    
    


