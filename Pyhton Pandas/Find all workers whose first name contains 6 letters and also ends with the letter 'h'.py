# cook your dish here

"""
Find all workers whose first name contains 6 letters and also ends with the letter 'h'


Amazon
Hard
General Practice
ID 9842
2
0
Find all workers whose first name contains 6 letters and also ends with the letter 'h'.


"""

# Import your libraries
import pandas as pd

# Start writing code
df=worker

df['name_len']=worker['first_name'].apply(len)
df['last_char']=worker['first_name'].str[-1]
df.loc[(df['name_len']==6)&(df['last_char']=='h')]
