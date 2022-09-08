import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler

df = pd.read_csv('E:\PTDL\OnlineRetail.csv', encoding='ISO-8859-1')

df.info()
df.isna()

# loại bỏ dữ liệu khuyết thiếu
df1 = df.dropna()

# % số lượng bản ghi còn lại
100 * df1.shape[0]/df.shape[0]

# Thay thế giá trị khuyết thiếu của thuộc tính Description bằng giá trị mặc định “Không biết”
df['Description'] = df['Description'].fillna('Khong biet')

df.info()

# vẽ box plot cho dữ liệu ở cột Quantity
sns.boxplot(x=df['Quantity'])
plt.show()

del df1
# Giá trị ngoại lai của thuộc tính Quantity chứa giá trị <0
df1 = df.drop(df[(df['UnitPrice'] <= 0)].index, inplace=False)
df1.info()

df2 = df1.drop(df1[(df1['Quantity'] <= 0)].index, inplace=False)
df2.info()
# vẽ box plot cho dữ liệu ở cột Quantity
sns.boxplot(x=df2['Quantity'])
plt.show()

df2.describe()
Q1 = df2.quantile(0.25)
Q3 = df2.quantile(0.75)
IQR = Q3-Q1

df3 = df2[~((df2 < (Q1 - 1.5 * IQR)) | (df2 > (Q3 + 1.5 * IQR))).any(axis=1)]
df4 = df3[['Quantity', 'UnitPrice']]
df4.describe()
df4.boxplot()
plt.show()
sns.kdeplot(data = df4)
plt.show()
# Chuẩn hóa dữ liệu cột Quantity
# phân bố dữ liệu trên cột Quantity
sns.kdeplot(data = df3['Quantity'])
plt.show()

