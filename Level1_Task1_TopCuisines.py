
"""
Created on Tue Aug 29 04:14:26 2023

@author: M.Nasir
"""

""" 
Level 1

Task1: Top Cuisines

    Determine the top three most
    common cuisines in the dataset.
    
    Calculate the percentage of
    restaurants that serve each of the top
    cuisines. 
    
"""
# Import Essential Libraries with their alias
import pandas as pd
from matplotlib import pyplot as plt

# First we Load our dataset using pandas
data = pd.read_csv('Dataset.csv')
# Seeing first 5 rows of Data
print(data.head())
# Seeing Shape of Data
print(data.shape)
# Seeing Cuisines column only
cuisines_col = data['Cuisines']
print(cuisines_col)
# Determining the top three most common cuisines in the dataset.
top_cuisines = cuisines_col.value_counts().head(3)
print("The Top Three Cuisines are:\n",top_cuisines)
# Total number of restaurants serving all Cuisines
total_Restaurants = len(data)
print("The Total Number of Restaurants is:\n",total_Restaurants)
# Calculating Percentages of Restaurants serving Top 3 Cuisines
percentages_of_Restaurants = (top_cuisines.values / total_Restaurants) * 100
print("The List of Percentage of Restaurants Serving Top 3 Cuisines is:\n",percentages_of_Restaurants)
# Ploting the Data in a Bar Plot
plt.bar(top_cuisines.index, percentages_of_Restaurants)
# X Label of Bar plot
plt.xlabel('Top Cuisines')
# Y Label of Bar Plot
plt.ylabel("Percentage")
# Title of Bar Plot
plt.title("Percentage of Restaurants serving Top 3 Cuisines")
# Rotation of X_Values of Bar Plot
plt.xticks(rotation = 0)
# Tight Layout of Bar Plot
plt.tight_layout()
# Seeing Bar plot
plt.show()