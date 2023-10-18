
"""
Created on Fri Sep  8 19:38:12 2023

@author: M.Nasir
"""
"""
Level3:
    Task1: Restaurant Reviews
    
    Analyze the text reviews to identify the most
    common positive and negative keywords.
    
    Calculate the average length of reviews and
    explore if there is a relationship between
    review length and rating.

"""
import pandas as pd
from matplotlib import pyplot as plt
data = pd.read_csv("Dataset.csv")
print("First 5 rows of Dataset", data.head())
print("The shape of dataset is:\n", data.shape)
print("The columns of dataset is:\n", data.columns)
text_review_count = data['Rating text'].value_counts()
print(text_review_count)

# Plotting
plt.figure(1)
# colors = ['green', 'black', 'red', 'hotpink', 'blue']
plt.bar(text_review_count.index, text_review_count.values)
plt.title("Text Reviews with their total occurence", size = 21)
plt.xlabel("Text Reviews", size = 17)
plt.ylabel("Text_Review_Count", size = 17)
plt.grid(color = 'black', linestyle = '--', linewidth = .5, alpha = .6)
plt.xticks()
plt.tight_layout()

# Average review length
data['review length'] = data['Rating text'].apply(lambda x: len(str(x).split()))
print(data['review length'])
average_review_length = data['review length'].mean()
print("Average Review Length:",average_review_length)

# a relationship between review length and rating.
relationship_bw_rev_len_and_rating = data.groupby('review length')['Aggregate rating'].mean()
print(relationship_bw_rev_len_and_rating)
relationship_bw_rev_len_and_rating = data.groupby('Aggregate rating')['review length'].mean()
print(relationship_bw_rev_len_and_rating)
r = relationship_bw_rev_len_and_rating 
# Plotting
plt.figure(2)
plt.scatter(r.index, r.values)
plt.xlabel("Ratings")
plt.ylabel("Review Length")
plt.title("Relationship between Review length and Rating ")
plt.xticks()
plt.tight_layout()