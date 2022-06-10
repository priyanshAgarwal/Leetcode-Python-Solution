# cook your dish here

"""
Number of Shipments Per Month


Interview Question Date: July 2021

Amazon
Easy
Active Interview
ID 2056
3
1
Write a query that will calculate the number of shipments per month. The unique key for one shipment is a combination of shipment_id and sub_id. Output the year_month in format YYYY-MM and the number of shipments in that month.



"""

# Import your libraries
import pandas as pd

# Start writing code
amazon_shipment.head()

df=amazon_shipment
# both will output Year-Month (Date Format)
df['year_month'] = amazon_shipment['shipment_date'].dt.strftime('%Y-%m')
df['year_month'] = df['shipment_date'].dt.to_period('M')

# size includes NaN values, count does not:
df.groupby('year_month').size().to_frame('num_of_shipment').reset_index()
df.groupby(['year_month']).count().reset_index()