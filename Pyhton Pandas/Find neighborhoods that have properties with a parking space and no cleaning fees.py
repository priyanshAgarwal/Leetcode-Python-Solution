# cook your dish here

"""
Find neighborhoods that have properties with a parking space and no cleaning fees


Find all neighborhoods that have properties with a parking space and don't charge for cleaning fees. 
"""

# Import your libraries
import pandas as pd

# Start writing code
airbnb_search_details.head()

df=airbnb_search_details.loc[(airbnb_search_details['cleaning_fee']==False) & (airbnb_search_details['amenities'].str.contains('parking'))]
df[['neighbourhood']].drop_duplicates()