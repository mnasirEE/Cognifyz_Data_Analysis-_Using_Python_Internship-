
"""
Created on Tue Aug 29 05:37:11 2023

@author: M. Nasir

"""

"""
Level 1

Task2: City Analysis

    Identify the city with the highest number
    of restaurants in the dataset.
    
    Calculate the average rating for
    restaurants in each city.
    
    Determine the city with the highest
    average rating.

"""
# Import Essential Python Libraries
# import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# First we Load our dataset using pandas
data = pd.read_csv('Dataset.csv')
# Seeing first 5 rows of Data
print(data.head())
# Seeing Shape of Data
print("The shape of DataSet is:",data.shape)

# Identifying the city with the highest number of restaurants in the dataset.
# 1st Method

print("The City which has the highest number of restaurants:")
print(data['City'].value_counts().head(1))

# 2nd Method
# Group data by city and count the number of restaurants
city_restaurant_count = data.groupby('City')['Restaurant Name'].count()
print(city_restaurant_count)
# Identifying the city with the highest number of restaurants in the dataset.
print("The City which has the highest number of restaurants: ",end ="")
print(city_restaurant_count.idxmax())


#  Calculating the average rating for restaurants in each city.

average_rating = data.groupby('City')['Aggregate rating'].mean()
print("The average rating for each city is:")
print(average_rating.head())

# Determining the city with the highest average rating.

print("City with the Highest average rating is:",end="")
print(average_rating.idxmax())

""" Ploting """

# Ploting of the average rating for restaurants in each city.

plt.bar(average_rating.index, average_rating.values, color = 'g')
plt.xlabel('City Names')
plt.ylabel("average rating")
plt.title("The Average rating of Cities")
plt.tight_layout()
plt.xticks(rotation = 90)
plt.show()

# Ploting of the Sorted average rating for restaurants in each city.

sorted_average_rating = average_rating.sort_values(ascending = False)
print("The sorted average rating is:")
print(sorted_average_rating)
plt.bar(sorted_average_rating.index, sorted_average_rating.values)
plt.xlabel('Sorted_City Names')
plt.ylabel("Sorted_average rating")
plt.title("The Sorted Average rating of Sorted_Cities")
plt.tight_layout()
plt.xticks(rotation = 90)
plt.show()

# Create a bar plot of cities with their restaurant count in given order

plt.bar(city_restaurant_count.head().index, city_restaurant_count.head().values, color = 'g')
plt.xlabel('City Names')
plt.ylabel("Restaurant Count")
plt.title("The Cities having number of Restaurants")
plt.tight_layout()
plt.xticks(rotation = 90)
plt.show()

# Create a bar plot of cities with their restaurant count in sorted order

sorted_city_restaurant_count = city_restaurant_count.sort_values(ascending = False)
print("The Sorted Cities with their restaurant counts")
print(sorted_city_restaurant_count)
plt.bar(sorted_city_restaurant_count.head().index, sorted_city_restaurant_count.head().values)
plt.xlabel('Sorted_City Names')
plt.ylabel("Sorted Restaurant Count")
plt.title("The Sorted Cities having number of Restaurants")
plt.tight_layout()
plt.xticks(rotation = 90)
plt.show()
