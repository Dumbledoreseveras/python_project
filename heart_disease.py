
"""Heart_disease.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IV3kWYZlcM1rIdQLJsVT7phcfbozSEqP
"""

import numpy as np
import matplotlib.pyplot as mtp
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data_set= pd.read_csv('/content/framingham.csv')

data_set.head()

data_set.shape

data_set.info()

data_set.describe().transpose()

"""**Filtering Dataset**"""

data_set.shape

data_set.isnull()

data_set.isnull().sum()/len(data_set) *100

import missingno as msno

msno.bar(data_set)
mtp.show()

msno.matrix(data_set)
mtp.show()

import missingno as msno
msno.heatmap(data_set)
mtp.show()

"""**Dealing with missing values**"""

data_set=data_set.dropna()

data_set.isnull().sum()*100/len(data_set)

data_set['TenYearCHD'].value_counts()

X = data_set.drop(columns='TenYearCHD',axis=1)
Y = data_set['TenYearCHD']

print(X)

print(Y)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

model=LogisticRegression()

model.fit(X_train, Y_train)

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on Training data: ',training_data_accuracy)

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on Test data: ',test_data_accuracy)

from math import e
input_data = (0,63,1,0,0,0,0,0,0,205,138,71,33.11,60,85)

input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]== 0):
  print('The person doesnot have Heart Disease')
else:
  print('The person has Heart Disease')