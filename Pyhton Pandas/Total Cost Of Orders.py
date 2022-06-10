# cook your dish here

"""
Total Cost Of Orders


Interview Question Date: July 2020

Amazon
Easy
Interview Questions
ID 10183
5
2
Find the total cost of each customer's orders. Output customer's id, first name, and the total order cost. Order records by customer's first name alphabetically.

"""

# Import your libraries
import pandas as pd

# Start writing code
customers.head()

df=customers.merge(orders,how='inner',right_on='cust_id',left_on='id')
df.groupby(['cust_id','first_name'])['total_order_cost'].sum().reset_index()