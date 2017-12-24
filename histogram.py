import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


df = pd.read_csv('./data/weight-height.csv')

males = df[df['Gender'] == 'Male']
females = df[df['Gender'] == 'Female']

males['Height'].plot(kind='hist', bins=50, range=(50,80), color='blue', alpha=0.3)
females['Height'].plot(kind='hist', bins=50, range=(50,80), color='red', alpha=0.3)

plt.title('Height distribution')
plt.legend(['Male', 'Female'])
plt.xlabel('Height (in)')

# Draw the vertical line at the mean
plt.axvline(males['Height'].mean(), color='blue', linewidth=2)
plt.axvline(females['Height'].mean(), color='red', linewidth=2)

#
# Histogram 2
#
males['Height'].plot(kind='hist', bins=200, range=(50,80), color='blue', alpha=0.3,
                    cumulative=True, normed=True)
females['Height'].plot(kind='hist', bins=200, range=(50,80), color='red', alpha=0.3,
                     cumulative=True, normed=True)

plt.show()