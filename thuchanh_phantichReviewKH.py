import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler


df = pd.read_csv('E:\PTDL\Credit_Scoring.csv')
df.head()

df.info()
# mô tả dữ liệu
df.describe()

# kiểm tra dữ liệu khuyết thiếu
df.isna()

# loại bỏ dữ liệu khuyết thiếu
df1 = df.dropna()

# % số lượng bản ghi còn lại
100 * df1.shape[0]/df.shape[0]

## vẽ biểu đồ phân bố 'MonthlyIncome'
sns.kdeplot(data=df1['MonthlyIncome'])
plt.show()

# thay thế dữ liệu khuyết thiếu bởi giá trị nội suy theo cột
df2 = df.interpolate(axis=1)

df2.isna()

#Xử lý dữ liệu ngoại lai
df2.boxplot()
plt.show()

# vẽ biểu đồ box plot cho MonthlyIncome
sns.boxplot(df2['MonthlyIncome'])
plt.show()

# tính giá trị Q1 và Q3
Q1 = df2.quantile(0.25)
Q3 = df2.quantile(0.75)

# tính IQR 
IQR = Q3 - Q1

# lọc dữ liệu ngoại lai
df3 = df2[~((df2<(Q1 - 1.5*IQR)) | (df2 > (Q3 + 1.5*IQR))).any(axis=1)]

df3.boxplot()
plt.show()

sns.boxplot(df3['MonthlyIncome'])
plt.show()

df3['MonthlyIncome'].describe()

#Chuẩn hóa dữ liệu
# Chuẩn hóa trên cột MonthlyIncome
# phân bố dữ liệu trên cột MonthlyIncome
sns.kdeplot(data=df3['MonthlyIncome'])
plt.show()

# chuẩn hóa với minmax scaling
scaler = MinMaxScaler()

mms = scaler.fit_transform(pd.DataFrame(df3['MonthlyIncome']))

sns.kdeplot(data=mms)
plt.show()

# chuẩn hóa với robust scaling
scaler = RobustScaler()

rbs = scaler.fit_transform(pd.DataFrame(df3['MonthlyIncome']))

sns.kdeplot(data = rbs)

# chuẩn hóa với standard scaling
scaler = StandardScaler()

sc = scaler.fit_transform(pd.DataFrame(df3['MonthlyIncome']))

sns.kdeplot(data = sc)
