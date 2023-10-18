# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 13:58:17 2023

@author: vc
"""

"""
Level3
    Task3: Price Range vs. Online Delivery and Table Booking
    
        Analyze if there is a relationship between the
        price range and the availability of online
        delivery and table booking.
        
        Determine if higher-priced restaurants are
        more likely to offer these services.

"""
import pandas as pd
from matplotlib import pyplot as plt
data = pd.read_csv("Dataset.csv")
print("First 5 rows of Dataset", data.head())
print("The shape of dataset is:\n", data.shape)
print("The columns of dataset is:\n", data.columns)

# relationship between the price range and the availability of online delivery

price_range_vs_online_delivery = data.groupby('Has Online delivery')['Price range'].mean()
print(price_range_vs_online_delivery)
# Plotting
plt.figure(1)
plt.bar(price_range_vs_online_delivery.index, price_range_vs_online_delivery.values)
plt.xlabel("Online Delivery")
plt.ylabel("Price Range")
plt.title("Price Range Vs Online Delivery")
plt.xticks(rotation = 0)
plt.tight_layout()

# relationship between the price range and the availability of table booking

price_range_vs_table_booking = data.groupby('Has Table booking')['Price range'].mean()
print(price_range_vs_table_booking)
plt.figure(2)
plt.bar(price_range_vs_table_booking.index, price_range_vs_table_booking.values)
plt.xlabel("Table Booking")
plt.ylabel("Price Range")
plt.title("Price Range Vs Table Booking")
plt.xticks(rotation = 0)
plt.tight_layout()

# relationship between the price range and the availability of online delivery and table booking
price_range_vs_online_delivery_and_table_booking = data.groupby(['Has Table booking', 'Has Online delivery'])['Price range'].mean()
print(price_range_vs_online_delivery_and_table_booking)

# Group the data by 'Has Online delivery' and 'Has Table booking' and calculate the mean price range
price_range_vs_online_delivery_and_table_booking = data.groupby(['Has Table booking', 'Has Online delivery'])['Price range'].mean()

# Convert the grouped data to a DataFrame for easy plotting
price_range_vs_online_delivery_and_table_booking_df = price_range_vs_online_delivery_and_table_booking.reset_index()
print(price_range_vs_online_delivery_and_table_booking_df)

# Define the labels for the bars
labels = ['No Table Booking & No Online Delivery', 'No Table Booking & Online Delivery', 'Table Booking & No Online Delivery', 'Table Booking & Online Delivery']

# Define the x-axis positions for the bars
x = range(len(price_range_vs_online_delivery_and_table_booking_df))
print(x)

# Plot the grouped bar chart
plt.figure(3)
plt.bar(x, price_range_vs_online_delivery_and_table_booking_df['Price range'])
plt.xlabel("Combination of Table Booking and Online Delivery")
plt.ylabel("Mean Price Range")
plt.title("Price Range Vs Combination of Table Booking and Online Delivery")
plt.xticks(x, labels, rotation=90)
plt.tight_layout()

plt.show()

print(price_range_vs_online_delivery_and_table_booking_df['Price range'])


# Determine if higher-priced restaurants are more likely to offer these services.
""" 'higher-priced restaurants are more likely to offer these services analysis', it is true after analysis of plots of table booking and online booking """