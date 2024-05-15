import time

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import seaborn as sns

import matplotlib.pyplot as plt
df = pd.read_csv('../data/Breast_Cancer.csv')
print(df.shape)
print(df.describe().to_latex(float_format='%.2f'))
print(df.columns)
'''
for column in df.columns:
    for column in df.columns:
        if df[column].dtype == 'object':  # Assuming 'object' type for categorical data
            plt.figure(figsize=(9, 5))
            sns.countplot(x=column, data=df)
            plt.title(f'Frequency of {column}')
            plt.show()
        else:  # Numerical data
            fig, axes = plt.subplots(1, 2, gridspec_kw={'width_ratios': [1, 4]}, figsize=(9, 5))
            df.boxplot(column=column, ax=axes[0])
            df.hist(column=column, ax=axes[1])
            plt.show()
        time.sleep(2)

df=df.dropna()
print(df.shape)
'''
plt.figure(figsize=(9, 5))
sns.countplot(x=, data=df)
plt.title(f'Frequency of {column}')
plt.show()

'''
local_outlier_factor = LocalOutlierFactor(n_neighbors=20)
result = local_outlier_factor.fit_predict(Credit['MarketPrice'].values.reshape(-1, 1))

outliers = result == -1
no_outliers = result == 1

feature extraction = ratio of tumor size and survival months
Credit['FinancingRatio'] = 100*Credit.AmountRequested/Credit.MarketPrice
Credit.FinancingRatio.hist(figsize=(8,8));'''