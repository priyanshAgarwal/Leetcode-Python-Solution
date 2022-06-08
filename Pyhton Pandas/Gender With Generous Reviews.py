# cook your dish here

"""
Gender With Generous Reviews


Interview Question Date: June 2020

Airbnb
Easy
Interview Questions
ID 10149
6
0
Write a query to find which gender gives a higher average review score when writing reviews as guests. Use the from_type column to identify guest reviews. Output the gender and their average review score.
"""

# Import your libraries
import pandas as pd

# Start writing code
airbnb_reviews.head()

df = airbnb_reviews.merge(airbnb_guests, left_on='from_user', right_on='guest_id')
df=df.loc[df['from_type']=='guest']
df=df.groupby(['gender'])['review_score'].mean().reset_index()
df=df.nlargest(1,'review_score')