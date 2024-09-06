import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

df = pd.read_csv(CITY_DATA['chicago'])
df['Start Time'] = pd.to_datetime(df['Start Time'])
df['Day_of_week'] = df['Start Time'].dt.weekday
print(df['Day_of_week'])