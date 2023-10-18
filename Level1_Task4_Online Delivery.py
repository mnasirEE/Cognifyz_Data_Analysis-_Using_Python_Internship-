
"""
Created on Tue Aug 29 07:41:24 2023

@author: M.Nasir

"""
"""
Level 1

Task4:  Online Delivery

        Determine the percentage of restaurants
        that offer online delivery.
        
        Compare the average ratings of restaurants
        with and without online delivery.

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

#  Determine the percentage of restaurants that offer online delivery.

online_delivery_restaurant_count = data.groupby('Has Online delivery')['Restaurant Name'].count() 
print(online_delivery_restaurant_count)
for x in online_delivery_restaurant_count.index:
    if x == 'Yes':
        print("The number of Restaurant that has Online Delivery is:")
        total_online_delivery_restaurants = online_delivery_restaurant_count[x] 
        print(total_online_delivery_restaurants)
    else:
        print("Not Online Delivery")
        total_not_online_delivery_restaurants = online_delivery_restaurant_count[x]
# Checking any null value in Restaurant column
print(data['Restaurant Name'].isnull().values.any())
# Hence we can find total restaurants  
total_restaurant_count = len(data)        

percentage_of_online_delivery_restaurants = (total_online_delivery_restaurants / total_restaurant_count) * 100        
print(percentage_of_online_delivery_restaurants)        

# Compare the average ratings of restaurants with and without online delivery.

compare_online_offline_delivery = data.groupby('Has Online delivery')['Aggregate rating'].mean()
print(compare_online_offline_delivery)

plt.bar(compare_online_offline_delivery.index, compare_online_offline_delivery.values)
plt.xlabel('Online Delivery')
plt.ylabel('Average Rating')
plt.title("Comparison of average ratings of restaurants with & without online delivery.")
plt.xticks(rotation = 0)
plt.tight_layout()
plt.show()