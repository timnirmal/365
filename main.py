import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# get data in Real_estate_data.csv
df = pd.read_csv("Numpy/Real_estate(cleaned).csv")

# find mean of numerical columns
temp_mean = np.mean(df, axis=0)

# count numberical columns
#num_cols = df.argwhere(np.isnan(temp_mean)==False).squeeze()

#a = np.getfromtxt("Numpy/Real_estate(cleaned).csv", delimiter=',', skip_header=1, usecols=num_cols,skip_footer=df.shape[0]-1)
# print
print(temp_mean)

# sixth column smallest value of df
print(df.iloc[:,5].min())

# last column largest value
print(df.iloc[:,df.shape[1]-1].max())

# distribute into 5 bins according to area
df['area'] = pd.cut(df['area'], 5)

print(df['area'])

# count values in each range
print(df['area'].value_counts())

