###---donor list------
#this script will create a new csv of all donors from the newest event

import pandas as pd

#read csv
df = pd.read_csv("15_report.csv")

#create a subset with only the minimum required columns
sub = df[['First Name', 'Last Name', 'Email', 'Total Paid']]

#obtain information of only those who have donated to the event
donors = sub.loc[sub['Total Paid']!= 0.0]

#save new susbscribers list to csv
donors.to_csv('donors.csv', index = False)
