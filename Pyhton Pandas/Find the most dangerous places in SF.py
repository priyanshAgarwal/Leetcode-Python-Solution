# cook your dish here

"""
Find the most dangerous places in SF


City of San Francisco
Easy
General Practice
ID 9749
1
0
Find the most dangerous places in SF based on the crime count per address and district combination.
Output the number of incidents alongside the corresponding address and the district.
Order records based on the number of occurrences in descending order.

"""

# Import your libraries
import pandas as pd

# Start writing code
sf_crime_incidents_2014_01.head()

df=sf_crime_incidents_2014_01.groupby(['address','pd_district'])['incidnt_num'].count().reset_index()
df.sort_values('incidnt_num', ascending=False)


# Import your libraries
import pandas as pd

# Start writing code
sf_crime_incidents_2014_01.head()
df=sf_crime_incidents_2014_01.groupby(['address','pd_district'])['incidnt_num'].count().reset_index().sort_values(by='incidnt_num',ascending=False)
