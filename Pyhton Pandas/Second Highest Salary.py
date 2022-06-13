# cook your dish here

"""
Second Highest Salary


Interview Question Date: April 2019

Amazon
Medium
Interview Questions
ID 9892
3
0
Find the second highest salary of employees.


"""

df['rnk']=df['salary'].rank(method='dense',ascending=False)
result=df[df['rnk']==2]['salary']


employee.head()
employee['salary'].nlargest(2)