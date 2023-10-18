
"""
Created on Tue Aug 29 10:18:31 2023

@author: M.Nasir

"""

"""
Task3:  Price Range Distribution

        Create a histogram or bar chart to
        visualize the distribution of price ranges
        among the restaurants.
        
        Calculate the percentage of restaurants
        in each price range category.

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

# Create a histogram or bar chart to visualize the distribution of price ranges among the restaurants.
Restaurants = data['Restaurant Name']
print(Restaurants.head())
price_ranges = data['Price range']
print(price_ranges.head())
plt.bar(Restaurants.head(5).values, price_ranges.head(5).values)
plt.xlabel('Restaurant Names')
plt.ylabel('Price Ranges')
plt.title("Distribution of Price ranges among the Restaurants")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.show()

# Calculate the percentage of restaurants in each price range category.

price_range_restaurant_count = data.groupby('Price range')['Restaurant Name'].count()
print(price_range_restaurant_count)
# Checking any null value in Restaurant column
print(data['Restaurant Name'].isnull().values.any())
restaurants_count = len(data)
percentage_of_restaurants_in_price_range = (price_range_restaurant_count / restaurants_count) * 100
print("the percentage of restaurants in each price range category.")
print(percentage_of_restaurants_in_price_range)

# Plotting of the percentage of restaurants in each price range category.

plt.plot(percentage_of_restaurants_in_price_range.index,percentage_of_restaurants_in_price_range.values, 'o-r', ms = 15, mfc = 'y', lw = 4.7)
plt.xlabel('Price Range (1 - 4)', color = 'b')
plt.ylabel("Percentage of Restaurants" , color = 'b')
plt.title("The Percentage of Restaurants with respect to Price range (1 - 4)", color = 'g')
plt.xticks(rotation = 45, color = 'r')
plt.tight_layout()
plt.show()