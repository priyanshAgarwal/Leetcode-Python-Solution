# cook your dish here

"""
Gender With Most Doctor Appointments


HealthTap
Easy
General Practice
ID 10170
4
0
Find the gender that has made the most number of doctor appointments.
Output the gender along with the corresponding number of appointments.


"""

# Import your libraries
import pandas as pd

# Start writing code

df=medical_appointments.groupby(['gender'])['appointmentid'].count().reset_index()

df.nlargest(1,'appointmentid')