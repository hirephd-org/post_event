##---new event subscribers list------
#this script will create a new csv of all subscribers from the newest event

import pandas as pd

#read csv
df = pd.read_csv("15_report.csv")

#create a subset with only the minimum columns
sub = df[['First Name', 'Last Name', 'Email', 'Do you agree to receive future events and news from the event organizers?']]

#obtain information of only those who wish to subscribe to our newsletter
subscribers = sub.loc[sub['Do you agree to receive future events and news from the event organizers?']=='Yes, sign me up!']

#save new susbscribers list to csv
subscribers.to_csv('new_subsribers.csv')
