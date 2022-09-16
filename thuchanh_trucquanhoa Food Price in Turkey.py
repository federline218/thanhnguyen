import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder

df = pd.read_csv('E:\PTDL\FoodPrice_in_Turkey.csv') 
df.head()

# Chọn dữ liệu cần thiết cho mục tiêu 1.
data1 = df[(df['Year'] == 2019) & (df['Month'] == 12) & (df['ProductName'] == 'Rice - Retail')]
data1

# Vẽ biểu đồ cột
plt.bar(data1['Place'], data1['Price'])
plt.show()

# Tinh chỉnh thuộc tính biểu đồ
plt.bar(data1['Place'], data1['Price'], width = 0.5)
plt.title('Rice Price in 12/2019', fontsize = 16, color = 'r')
plt.xlabel('Place', fontsize = 14)
plt.ylabel('Price', fontsize = 14)
plt.show()

# Chọn dữ liệu cần thiết cho mục tiêu 2 
data2 = df[(df['Place'] == 'National Average') & (df['Year'] == 2019) & (df['ProductName'] == 'Rice - Retail')]
# Vẽ biểu đồ đường
plt.plot(data2['Month'], data2['Price'])
plt.show()

# Tinh chỉnh thuộc tính biểu đồ đường
plt.plot(data2['Month'], data2['Price'], linewidth = 2, marker = '*', markersize=10, markerfacecolor='red', markeredgecolor = 'blue', markeredgewidth=2)
plt.title('Rice Price of National Average in 2019', fontsize = 16, color = 'r')
plt.xlabel('Month', fontsize = 14)
plt.ylabel('Price', fontsize = 14)
plt.show()

# Chọn dữ liệu cần thiết cho mục tiêu 3
x = df[(df['Place'] == 'National Average') & (df['ProductName'] == 'Fuel (gas) - Retail') & (df['Year'] == 2019)]
y = df[(df['Place'] == 'National Average') & (df['ProductName'] == 'Rice - Retail') & (df['Year'] == 2019)]

plt.scatter(x['Price'], y['Price'])
plt.show()

# Tinh chỉnh biểu đồ Scatter
plt.scatter(x['Price'], y['Price'], s = 50)
plt.title('Relationship between Rice Price and Gas Price', fontsize = 16, color = 'r')
plt.xlabel('Gas', fontsize = 14)
plt.ylabel('Rice', fontsize = 14)
plt.show()