import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


df = pd.read_csv('./data/international-airline-passengers.csv')
print(df.info())
print(df.head())

# change column type 'Month' to dataime type
df['Month'] = pd.to_datetime(df['Month'])

# Set index for dataframe
df  = df.set_index('Month')

# create line plot (default)
df.plot()
plt.show()