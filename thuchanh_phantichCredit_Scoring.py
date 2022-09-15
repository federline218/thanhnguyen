import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from Pandas.thuchanh_xulybodulieuOnlineRetail import IQR

df = pd.read_csv("Credit_Scoring.csv")
df.head()
# Nêu thông tin về kiểu dữ liệu và khoảng dữ liệu ở các cột
df.info()
df.shape

#Kiểm tra dữ liệu khuyết thiếu
df.isna().sum()

# Thay thế giá trị khuyết thiếu bằng giá trị nội suy theo các cột
df['MonthlyIncome'].interpolate(method='linear', axis=0, limit_direction ='backward', inplace=True)

df.isnull().sum()

df['MonthlyIncome'].iloc[:40]

df['NumberOfDependents'].interpolate(method='linear', axis=0, limit_direction ='backward', inplace=True)
df['NumberOfDependents'].iloc[:40]

#Vẽ biểu đồ boxplot, biểu đồ phân bố dữ liệu cho các cột
for var in df.columns:
    plt.figure(figsize=(15,6))
    plt.subplot(1, 2, 1)
    fig = df.boxplot(column=var)
    fig.set_title('')
    fig.set_ylabel(var)

    plt.subplot(1, 2, 2)
    fig = df[var].hist(bins=20)
    fig.set_ylabel('')
    fig.set_xlabel(var)

    plt.show()
    
df = df.drop(df.columns[[0]], axis=1) # xóa cột đầu tiên

# Loại bỏ giá trị ngoại lai
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 -Q1

print(IQR)

df2 = df[~((df < (Q1 - 1.5*IQR)) | (df > (Q3 + 1.5*IQR))).any(axis=1)]

# Chia dữ liệu ở các cột thành 4,5,6 nhóm có số lượng phần tử bằng nhau và đếm số lượng phần tử ở mỗi nhóm, lấy ra khoảng giữ liệu của mỗi nhóm.
cats = pd.qcut(df['RevolvingUtilizationOfUnsecuredLines'], 4)
cats
pd.value_counts(cats)

def split_var(col, n):
    cats = pd.qcut(col, n)
    print(cats)
    print(pd.value_counts(cats))   

split_var(df['RevolvingUtilizationOfUnsecuredLines'], 5)

# Chia dữ liệu ở các cột age và MonthlyIncome thành 5 nhóm theo các khoảng: 0, 30, 40, 50, 80, 150 và đếm số lượng phần tử ở mỗi nhóm.
# định nghĩa khoảng giá trị các nhóm
# danh sách tên
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior', 'Old']
bins = [0, 30, 40, 50, 80, 150]
cats = pd.cut(df['age'], bins, labels=group_names)
cats
pd.value_counts(cats)

