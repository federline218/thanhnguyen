import pandas as pd
import numpy as np

df = pd.read_csv('E:\PTDL\shopeep_koreantop_clothing_shop_data.csv')
df.head()

# Tách cột shop_location thành 2 cột District và City
df['District'] = df['shop_location'].str.split(',').str[0]
df['City'] = df['shop_location'].str.split(',').str[1]
df.head(10)

# Tách cột date_collected thành 3 cột Day, Month, Year
df['Day'] = pd.to_datetime(df['date_collected'], format='%Y-%m-%d').dt.day
df['Month'] = pd.to_datetime(df['date_collected'], format= '%Y-%m-%d').dt.month
df['Year'] = pd.to_datetime(df['date_collected'], format='%Y-%m-%d').dt.year
df.head(15)

# Tách cột response_time thành 3 cột Hour, Minute, Second
df['Hour'] = pd.to_datetime(df['response_time'], format=' %H:%M:%S').dt.hour
df['Minute'] = pd.to_datetime(df['response_time'], format=' %H:%M:%S').dt.minute
df['Second'] = pd.to_datetime(df['response_time'], format=' %H:%M:%S').dt.second
df.head(10)
