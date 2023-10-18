
"""
Created on Fri Sep  8 16:47:47 2023

@author: M.Nasir
"""

"""
Level 2

    Task: Cuisine Combination

    Identify the most common combinations of
    cuisines in the dataset.
    Determine if certain cuisine combinations
    tend to have higher ratings.
"""  
# Answer
import pandas as pd
from matplotlib import pyplot as plt
data = pd.read_csv("Dataset.csv")
print("First 5 rows of Dataset", data.head())
print("The shape of dataset is:\n", data.shape)
print("The list of columns of dataset is:\n",data.columns)
most_common_comb_cuisines = data['Cuisines'].value_counts()
print("First 10 most common combination of Cuisines:\n", most_common_comb_cuisines.head(10))
print(" The Shape of column of most common combination of cuisines is", most_common_comb_cuisines.shape)
cuisine_comb_with_higher_rating = data.groupby('Cuisines')['Aggregate rating'].mean()
print("First 35 random records of certain cuisine combinations tend to have higher ratings:\n ", cuisine_comb_with_higher_rating.head(30))
sorted_cuisine_comb_with_higher_rating = cuisine_comb_with_higher_rating.sort_values(ascending = False)
print("First 35 records of sorted certain cuisine combinations tend to have higher ratings:\n ", sorted_cuisine_comb_with_higher_rating.head(30))
print("The Shape of  certain cuisine combinations tend to have higher ratings: ",sorted_cuisine_comb_with_higher_rating.shape)

# Plotting
# Plotting of most common combination of cuisines
plt.figure(1)
plt.bar(most_common_comb_cuisines.head(10).index, most_common_comb_cuisines.head(10).values)
plt.title("The Most Common Combinations of Cuisines")
plt.xlabel("Cuisine Combination")
plt.ylabel("Cuisine Combination Count")
plt.xticks(rotation = 90)
plt.tight_layout()

plt.figure(2)
# Plotting of certain cuisine combination that tend to have higher rating
plt.bar(cuisine_comb_with_higher_rating.head(15).index, cuisine_comb_with_higher_rating.head(15).values)
plt.title("Certain Cuisine Combinations with Higher Ratings")
plt.xlabel("Cuisine Combination")
plt.ylabel("Average Rating")
plt.xticks(rotation = 90)
plt.tight_layout()



