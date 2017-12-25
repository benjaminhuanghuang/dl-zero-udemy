import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


df = pd.read_csv('./data/weight-height.csv')
print(df.info())
print(df.head())
print(df.describe())

print('Vaule contents of Gender: ', df['Gender'].value_counts())
#
# Create scatter plot 1
#
_ = df.plot(kind='scatter', x='Height', y='Weight')
#
# Create scatter plot 2
#
males = df[df['Gender'] == 'Male']
females = df[df['Gender'] == 'Female']
# Create a figure and a set of subplots
fig, ax = plt.subplots() 

males.plot(kind='scatter', x='Height', y='Weight', ax=ax, color='blue', alpha=0.3,
           title='Male and Female Populations')

females.plot(kind='scatter', x='Height', y='Weight',
             ax=ax, color='red', alpha=0.3)
#
# Create scatter plot 3
#             
# Create new data column
df['GenderColor'] = df['Gender'].map({'Male':'blue', 'Female':'red'})
df.plot(kind='scatter', x='Height', y='Weight',
            color =df['GenderColor'], alpha=0.3)
plt.show()