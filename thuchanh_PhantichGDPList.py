import pandas as pd
import numpy as np

df = pd.read_csv('E:\PTDL\GDPlist.csv', encoding = "ISO-8859-1")
df.shape
df.info()

# Tính giá trị lớn nhất và nhỏ nhất của GDP.
min_GDP = df['GDP (millions of US$)'].min()
min_GDP

max_GDP = df['GDP (millions of US$)'].max()
max_GDP

df.describe()
df['GDP (millions of US$)'].mean()
df['GDP (millions of US$)'].median()
df['GDP (millions of US$)'].max()
df['GDP (millions of US$)'].min()

#chau luc xuat hien nhieu nhat
df['Continent'].mode()

#df.drop(['sum_GDP'], axis=1, inplace=True)

# tong GDP cua moi chau luc
df['sum_GDP'] = df['GDP (millions of US$)'].groupby(df['Continent']).transform('sum') #tao cot sum_GDP, gia tri la sum GDP cua cac chau luc   
df_sumGDP = df[['Continent','sum_GDP']].drop_duplicates() # tao df moi chi chua 2 cot chau luc va sum_GDP
df_sumGDP

# trung bình cộng GDP
df['mean_GDP'] = df['GDP (millions of US$)'].groupby(df['Continent']).transform('mean')
df_mean_GDP = df[['Continent','mean_GDP']].drop_duplicates()
df_mean_GDP

# hợp nhất 2 bảng trên
df_merge = pd.merge(df_sumGDP,df_mean_GDP, on='Continent')
df_merge

