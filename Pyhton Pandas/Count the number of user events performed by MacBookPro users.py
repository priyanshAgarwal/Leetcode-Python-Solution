# cook your dish here

"""
Count the number of user events performed by MacBookPro users


Apple
Easy
General Practice
ID 9653
5
2
Count the number of user events performed by MacBookPro users.
Output the result along with the event name.
Sort the result based on the event count in the descending order.


"""

# This is series, functions are different
macbook = playbook_events.loc[playbook_events['device'] == 'macbook pro','event_name'].value_counts().reset_index()

# This is dataframe, function is different
macbook = playbook_events.loc[playbook_events['device'] == 'macbook pro'].groupby(['event_name'])['user_id'].count().reset_index()