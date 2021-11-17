import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set()

#df_used_cars = pd.read_csv("Visualization\\bar_chart_data.csv")
df_bar = pd.read_csv("Visualization\\pie_chart.csv")

# show the data
print(df_bar)

# Set figure size
plt.figure(figsize=(9, 6))
plt.title("Used Cars", fontsize=20, fontweight='bold')
# Overlapping Labels
plt.xticks(rotation=45, fontsize=12)

# Bar chart
# plt.bar(df_used_cars["Brand"], df_used_cars["Cars Listings"])
plt.bar(df_bar["Cities"], df_bar["Sales"])

# pie chart
# Cities,Sales,Cumulative Frequency on pie_chart.csv
#plt.pie(df_used_cars["Cities"], labels=df_used_cars["Sales"], autopct='%1.1f%%')
# plt.pie(df_used_cars["Cars Listings"], labels=df_used_cars["Brand"], autopct='%1.1f%%')

# Area chart - Stack plot
# plt.stackplot(df_used_cars["Brand"], df_used_cars["Cars Listings"], labels=df_used_cars["Brand"], colors=['#0066ff', '#ff6600', '#00ff00'])

# Convert Date to datetime -  This will help to use correct data format
# df_used_cars["Date"] = pd.to_datetime(df_used_cars["Date"])

plt.show()
# plt.savefig("Visualization\\bar_chart.png")


# ggplot layers
# data
# aesthetic
