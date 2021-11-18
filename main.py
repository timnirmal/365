import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Pandas
df = pd.read_csv('data/data.csv')

start_date_deposit = pd.Series(
    {
        "01/01/2019": 2000,
        "02/01/2019": 2000,
        "03/01/2019": 2000,
        "04/01/2019": 2000,
    }
)

# sum of smallest and largest values in a series using implicit index
print(start_date_deposit.nsmallest(2).sum())

df = pd.DataFrame(nparray, columns=['date', 'amount'])

# typeof data frame
print(type(df))

# sql

# number of missing album names in album table sql

SELECT SUM(CASE WHEN album_name IS NULL THEN 1 ELSE 0 END)