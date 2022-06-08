# cook your dish here

"""
Submission Types


Interview Question Date: December 2020

Credit Karma
Easy
Active Interview
ID 2002
6
0
Write a query that returns the user ID of all users that have created at least one ‘Refinance’ submission and at least one ‘InSchool’ submission.


"""

df = loans[(loans['type'] == 'Refinance') | (loans['type'] == 'InSchool')]
df1 = df.groupby('user_id')['type'].nunique().reset_index()
df2 = df1[df1['type'] > 1]['user_id']
