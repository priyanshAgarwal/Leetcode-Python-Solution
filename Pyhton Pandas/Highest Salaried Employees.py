# cook your dish here

"""
Highest Salaried Employees


Amazon
Medium
General Practice
ID 9865
2
0
Find the employee with the highest salary in each department.
Output the department name, employee's first name, and the salary.


"""

# Import your libraries
import pandas as pd

# Start writing code
df=worker

# Important remove null before ranking
df=df[df['salary'].notnull()]

# df=df[df['salary'].notnull()]
# Using Dense Rank
df['rank']=df.groupby('department')['salary'].rank(method='dense',ascending=False)
df.loc[df['rank']==1,['department','first_name','salary']]
df[df['rnk']==1][['department','first_name','salary']]

# Using nlargest
df=worker.groupby('department').apply(lambda d:d.nlargest(1,columns='salary',keep='all'))
df[['department', 'first_name', 'salary']]