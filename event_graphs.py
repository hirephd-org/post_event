#this script will create an interactive graph using dash plotly
import pandas as pd

#read in evnetbrite report for a given event
df = pd.read_csv('15_report.csv')

#change 'Order Date' column to datetime dtype
df['Order Date'] = pd.to_datetime(df['Order Date'])

#extract year-month-date and create a new column 'date'
df['date'] = df['Order Date'].dt.to_period('D')
