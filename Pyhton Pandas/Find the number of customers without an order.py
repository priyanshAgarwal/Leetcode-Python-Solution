# cook your dish here

"""
Find the number of customers without an order


Amazon
Medium
General Practice
ID 10089
7
0
Find the number of customers without an order.
"""

# Import your libraries
import pandas as pd

# Start writing code
df=customers.merge(orders, how='left', left_on='id',right_on='cust_id')

df=df.loc[df['id_y'].isnull()]

len(df['id_x'].drop_duplicates())