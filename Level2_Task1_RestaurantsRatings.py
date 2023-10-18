
"""
Created on Fri Sep  1 01:12:03 2023

@author: M.Nasir

"""
import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt
import seaborn as sns

data = pd.read_csv("Dataset.csv")
print(data.head())
print(data.columns)
# Analyze the distribution of aggregate ratings and determine the most common rating range.

aggregate_rating = data['Aggregate rating']
print(aggregate_rating.head())
Restaurants = data["Restaurant Name"]
print(Restaurants.head())
# Analyze the distribution of aggregate ratings
def Scatter():
    plt.figure(5)
    sizes = np.random.randint(50, size = 200)
    #print(sizes)
    d = np.random.randint(100, size = 200)
    colors = d
    plt.scatter(Restaurants.head(200).values, aggregate_rating.head(200).values, s = sizes, c = colors, cmap ='nipy_spectral')
    plt.colorbar()
    plt.xticks(rotation = 90)
# Analyze the distribution of aggregate ratings
def Bar_Plot():
    plt.figure(1)
    plt.bar(Restaurants.head(25).values, aggregate_rating.head(25).values)
    plt.xlabel("Restaurant Names", color = 'b', size = 15 )
    plt.ylabel("Aggregate Rating", color = 'b', size = 15)
    plt.title("Bar plot of Aggregate Ratings", color = 'b', loc = 'left', size = 20)
    plt.xticks(rotation = 90)
    plt.tight_layout()



# Analyze the distribution of aggregate ratings by line plot
def Line_Plot():
    plt.figure(2)
    plt.plot(aggregate_rating.head(25).values, 'X--r', ms = 7.5, mec = 'y', mfc = 'g')
    plt.xlabel("x-axis", color = 'b', size = 15 )
    plt.ylabel("Aggregate Rating", color = 'b', size = 15)
    plt.title("Line plot of Aggregate Ratings", color = 'b', loc = 'left', size = 20)
    plt.xticks(rotation = 0)
    plt.tight_layout()
    plt.grid(color = 'k', linestyle = '--', linewidth = 1.5, alpha = .7)

# Analyze the distribution of aggregate ratings by histogram
def Histogram():
    plt.figure(3)
    plt.hist(aggregate_rating.head(25).values)
    plt.xlabel("Aggregate Rating", color = 'b', size = 15 )
    plt.ylabel("Frequency or Density", color = 'b', size = 15)
    plt.title("Distribution of Aggregate Ratings", color = 'b', loc = 'left', size = 20)
    plt.xticks(rotation = 0)
    plt.tight_layout()
    plt.grid(color = 'k', linestyle = '--', linewidth = 1.5, alpha = .7)

# Analyze the distribution of aggregate ratings by distribution plot using seaborn library
def Distribution_Plot():
    plt.figure(4)
    sns.distplot(aggregate_rating.head(25).values)
    plt.xlabel("Aggregate Rating", color = 'b', size = 15 )
    plt.ylabel("Frequency or Density", color = 'b', size = 15)
    plt.title("Distribution of Aggregate Ratings", color = 'b', loc = 'left', size = 20)
    plt.xticks(rotation = 0)
    plt.tight_layout()
    plt.grid(color = 'k', linestyle = '--', linewidth = 1.5, alpha = .7)
    
# determine the most common rating range.

most_common_rating = data['Aggregate rating'].value_counts().head(1)
print("most common rating is",most_common_rating)

# Calculate the average number of votes received by each restaurant.

average_number_of_votes = data.groupby('Restaurant Name')['Votes'].mean()
print(average_number_of_votes.head(7))
restaurant_max_votes = average_number_of_votes.sort_values(ascending = False).head(1)
r = list(restaurant_max_votes.index)
v = list(restaurant_max_votes.values)
l = [r[0],v[0]]
print(f"'{l[0]}' Restaurant got maximum votes of {l[1]}")
print(data['Votes'].head())
