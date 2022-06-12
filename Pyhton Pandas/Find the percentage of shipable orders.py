# cook your dish here

"""
Find the percentage of shipable orders


Amazon
Medium
General Practice
ID 10090
5
0
Find the percentage of shipable orders.
Consider an order is shipable if the customer's address is known.
"""

import pandas as pd

# Start writing code
df = pd.merge(orders, customers, how='left', left_on='cust_id', right_on='id')
df['is_ship']=(df['address'].notnull())
df['shipable'] = df['address'].isna().astype(int)

df['is_shipable']=df['address'].notnull().astype(int)

100.0*df['is_shipable'].sum()/len(df['is_shipable'])