'''
    Training => minimizing cost => best model
'''
import numpy as numpy
import pandas as pd
 
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam, SGD


df = pd.read_csv('./data/weight-height.csv')

X = df[['Height']].values
y_true = df['Weight'].values


model = Sequential()
model.add(Dense(1, input_shape(1,)))
model.summary()
model.compile(Adam(lr=0.8), 'mean_squared_error')
model.fit(X, y_true, epochs=40)
y_pred = model.predict(X)

df.plot(kind='scatter', x='Height', y= 'Weight', title='Weight and Height')

plot.show()

def mean_squared_error(y_true, y_pred):
    s = (y_pred - y_true) **2
    return s.mean()