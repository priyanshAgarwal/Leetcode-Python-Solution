# cook your dish here

"""
Favorite Customer

Interview Question Date: May 2019

Amazon

Medium

Interview Questions

Find "favorite" customers based on the order count and the total cost of orders.
A customer is considered as a favorite if he or she has placed more than 3 orders and with the total cost of orders more than $100.

Output the customer's first name, city, number of orders, and total cost of orders.
"""

# Import your libraries
import pandas as pd

# Start writing code
customers.head()
merge = pd.merge(customers, orders, how = 'right', left_on='id', right_on = 'cust_id')
total = merge.groupby(['first_name','city']).agg({'id_y':'count','order_cost':'sum'}).reset_index()
result = total[(total['id_y']> 3) & (total['order_cost']> 100)]