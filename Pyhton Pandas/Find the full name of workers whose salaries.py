# cook your dish here

"""
Find the full name of workers whose salaries >= 50000 and <= 100000


Amazon
Medium
General Practice
ID 9846
3
0
Find the full name of workers whose salaries >= 50000 and <= 100000
Output the worker's first name and last name in one column along with their salaries


"""

# Import your libraries
import pandas as pd

# Start writing code
worker.head()

df=worker.loc[ (worker['salary']>= 50000)&(worker['salary']<= 100000)]

df['Worker_Name']=df['first_name']+' '+df['last_name']
df.loc[:,['salary','Worker_Name']]
