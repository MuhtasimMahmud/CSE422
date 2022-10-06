# -*- coding: utf-8 -*-
"""2_19101652_Muhtasim Mahmud.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ssw6KYpkZvMdDgEe7xH7dSoM61-WIYZW
"""

#importing necessary libraries
import pandas as pd
import numpy as np

mydataset = pd.read_csv('Income Dataset (50k).csv')

print(mydataset.shape)
print(mydataset.shape[0])
print(mydataset.shape[1])

#Returning First 5 Values
print(mydataset.head())
print(mydataset.sample)
print(mydataset.columns)

#Handing The Missing Values

print(mydataset.isnull())
print(mydataset.isnull().sum())

#Dropping The Blank Rows

mydataset = mydataset.dropna(axis = 0, subset = ['workclass','occupation','native-country']) #row=0
print("Shape after dropping:", mydataset.shape)

#Encode Categorical Features
mydataset.info()
print(mydataset['income_>50K'].unique())
print(mydataset['relationship'].unique())
print(mydataset['workclass'].unique())

#Encodding Using The Level Encoder
from sklearn.preprocessing import LabelEncoder

# Set up the LabelEncoder object
enc = LabelEncoder()

# Apply the encoding to the "Workclass" column
mydataset['workclass'] = enc.fit_transform(mydataset['workclass'])

# Compare the two columns
print(mydataset['workclass'].head(10))

# Apply the encoding to the "education" column
mydataset['education'] = enc.fit_transform(mydataset['education'])
# Compare the two columns
print(mydataset['education'].head())
# Apply the encoding to the "gender" column
mydataset['gender'] = enc.fit_transform(mydataset['gender'])
# Compare the two columns
print(mydataset['gender'].head())
# Apply the encoding to the "occupation " column
mydataset['occupation'] = enc.fit_transform(mydataset['occupation'])
# Compare the two columns
print(mydataset['occupation'].head())
mydataset.info()
#Encoding 
print(mydataset['income_>50K'].unique())

#Splitting the dataset into features and labels.
from sklearn.model_selection import train_test_split
list_of_features=mydataset[['workclass','education','occupation','gender']]
targate_data = mydataset['income_>50K']

#Splitting The Data
x_train, x_test, y_train, y_test = train_test_split(list_of_features, targate_data, test_size=0.05, random_state=1)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

model = LogisticRegression()
#Model Training
model.fit(x_train, y_train) 
predictions = model.predict(x_test)
#Predictions Print
print(predictions)
print( accuracy_score(y_test, predictions))