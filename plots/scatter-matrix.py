import numpy as np
import pandas as pd
from pandas.tools.plotting import scatter_matrix

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


df = pd.read_csv('./data/titanic-train.csv')
print(df.head())

_ = scatter_matrix(df.drop('PassengerId', axis=1), figsize=(10,10))
plt.show()
