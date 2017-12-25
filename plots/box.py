import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


df = pd.read_csv('./data/weight-height.csv')
# put data into table, use the value of 'Gender' as the columns, the values came from 'Weight'
dfpvt = df.pivot(columns = 'Gender', values='Weight')
print('dfpvt data: ', dfpvt.head())
dfpvt.plot(kind='box')
plt.title('Weight Box Plot')
plt.ylabel('Weight (lbs)')

plt.show()