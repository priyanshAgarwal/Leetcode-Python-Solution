# cook your dish here

"""
Mobile and Web Logins


Interview Question Date: November 2021

Pinterest
Easy
Active Interview
ID 2080
4
1
Count the number of unique users per day who logged in from both a mobile device and web. Output the date and the corresponding number of users.


"""

# Import your libraries
import pandas as pd

all_users=mobile_logs.merge(web_logs, how='inner', left_on=['user_id','date'], right_on=['user_id','date']).drop_duplicates()
result=all_users.groupby(['date'])['user_id'].count().reset_index()