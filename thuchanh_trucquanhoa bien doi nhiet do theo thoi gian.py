import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('E:\PTDL\daily-min-temperatures.csv') 
df.head()

# Hiển thị các giá trị thống kê của dữ liệu nhiệt độ
df['Temp'].describe()

# Vẽ biểu đồ Histogram
plt.hist(df['Temp'], bins = 45)
plt.show()

# Tinh chỉnh biểu đồ
plt.hist(df['Temp'], bins=45, range=(1,23), histtype='step')
plt.title('Temperature Histogram', fontsize= 16)
plt.show()

# 7. Vẽ biểu đồ đường thể hiện xu hướng nhiệt độ
plt.plot(df['Date'], df['Temp'])
plt.title('Daily Temperature', fontsize = 16)
plt.xlabel('Date', fontsize = 14)
plt.ylabel('Temp', fontsize = 14)
plt.show()

# biểu đồ đường thể hiện xu hướng nhiệt độ theo từng năm quan tâm
df['Date'] = pd.to_datetime(df['Date'])
bounds = ['1/1/1990', '12/31/1990']
bounds = pd.to_datetime(bounds)
df1 = df[(df['Date'] >= bounds[0]) & (df['Date'] <= bounds[1])]
plt.plot(df1['Date'], df1['Temp'])
plt.title('Daily Temperature in 1990', fontsize = 16)
plt.xlabel('Date', fontsize = 14)
plt.ylabel('Temp', fontsize = 14)
plt.show()
