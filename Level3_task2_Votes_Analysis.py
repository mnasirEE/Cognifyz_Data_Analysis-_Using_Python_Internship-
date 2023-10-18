# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 21:22:22 2023

@author: vc
"""

"""
Level3
Task2: Votes Analysis

    Identify the restaurants with the highest and
    lowest number of votes.
    
    Analyze if there is a correlation between the
    number of votes and the rating of a
    restaurant.
"""
import pandas as pd
from matplotlib import pyplot as plt
data = pd.read_csv("Dataset.csv")
print("First 5 rows of Dataset", data.head())
print("The shape of dataset is:\n", data.shape)
print("The columns of dataset is:\n", data.columns)

#  Identify the restaurants with the highest and lowest number of votes.

sorted_votes = data.sort_values('Votes', ascending = False)
Res_Votes = data[['Restaurant Name', 'Votes']]
highest_vote = Res_Votes.sort_values(by = 'Votes', ascending = False).head(1)
print("Restaurant with Highest Vote:\n", highest_vote)
lowest_vote = Res_Votes.sort_values(by = 'Votes', ascending = True).head(1)
print("Restaurant with Lowest Vote:\n", lowest_vote)


# correlation between the number of votes and the rating of a restaurant.

correlation = data['Votes'].corr(data['Aggregate rating'])
print("Correlation between Votes and Aggregate rating:",correlation)
'''This code will calculate the Pearson correlation coefficient between the number of votes and the aggregate rating. A positive value indicates a positive correlation (more votes are associated with higher ratings), while a negative value indicates a negative correlation (more votes are associated with lower ratings).'''

# Plotting

plt.scatter(data['Votes'], data['Aggregate rating'])
plt.xlabel("Votes")
plt.ylabel("Aggregate Rating")
plt.title("Correlation Between Votes and Rating")