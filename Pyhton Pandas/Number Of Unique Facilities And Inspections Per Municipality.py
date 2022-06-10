# cook your dish here

"""
Number Of Unique Facilities And Inspections Per Municipality

Interview Question Date: April 2018

City of Los Angeles
Medium
Interview Questions
ID 9702
3
1
Count the number of unique facilities per municipality zip code along with the number of inspections. Output the result along with the number of inspections per each municipality zip code. Sort the result based on the number of inspections in descending order.


"""

# Import your libraries
import pandas as pd

# Start writing code

df=los_angeles_restaurant_health_inspections
# Only get first 5 letters
df['facility_zip']=df['facility_zip'].str[:5]

# groupby one column and then compute on other columns as well 
df=los_angeles_restaurant_health_inspections.groupby(['facility_zip']).agg({
    'facility_id':'nunique','record_id':'count'}).reset_index()
df.sort_values('record_id',ascending=False)

# Method 2
count_facilities = los_angeles_restaurant_health_inspections.groupby(['facility_zip'])['facility_id'].agg(no_facilities = 'nunique', no_inspections = 'count').reset_index()
