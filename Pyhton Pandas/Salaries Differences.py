# cook your dish here

"""
Salaries Differences


Interview Question Date: November 2020

Dropbox
Easy
Interview Questions
ID 10308
30
2
Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments. Output just the absolute difference in salaries.



"""

# Import your libraries
import pandas as pd

# Start writing code
df=db_employee.merge(db_dept, how='left',left_on='department_id',right_on='id')
df=df[["department","salary"]]

# df[df['department']=='marketing']['salary'].max()-df[df['department']=='engineering']['salary'].max()

df[df['department']=='marketing']['salary'].max()-df[df['department']=='engineering']['salary'].max()

# highest_marketing = df.loc[df['department'] == 'marketing']