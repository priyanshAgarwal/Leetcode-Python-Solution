# cook your dish here

"""
Expensive Projects


Interview Question Date: November 2020

Microsoft
Easy
Interview Questions
ID 10301
6
0
Given a list of projects and employees mapped to each project, calculate by the amount of project budget allocated to each employee . The output should include the project title and the project budget per employee rounded to the closest integer. Order your list by projects with the highest budget per employee first.


"""

import pandas as pd
import numpy as np

df=ms_projects.merge(ms_emp_projects, how = 'inner',left_on = ['id'], right_on=['project_id'])
df=df.groupby(['title','budget'])['emp_id'].count().reset_index()
df['budget_emp_ratio'] = (df['budget']/df['emp_id']).round(0) # To round by how many digits
df2=df.sort_values(by='budget_emp_ratio',ascending=False)
result = df2[["title","budget_emp_ratio"]]