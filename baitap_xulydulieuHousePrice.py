import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from scipy import stats



df = pd.read_excel('E:\PTDL\house_price_dống-da.xlsx')
df.head()
df.info()
df.describe()

df.isna()
#Xóa bỏ hết tất cả những dòng dữ liệu không có thông tin về giá
df1 = df.dropna(subset=['price'], inplace=False)
df1.info()

#Thay thế giá trị khuyết thiếu của land_certificate bằng =”không có thông tin”
df1['land_certificate'] = df1['land_certificate'].fillna('không có thông tin')
del df1

# Thay thế giá trị khuyết thiếu của house_direction, balcony_direction, toilet, bedroom, Floor  bằng giá trị có tần số xuất hiện lớn nhất của các thuộc tính đó
df1.info()
#modevalue = df1[['house_direction', 'balcony_direction', 'toilet', 'bedroom', 'floor']].mode()[0]
#print(modevalue)
cols = ['house_direction', 'balcony_direction', 'toilet', 'bedroom', 'floor']
df1[cols] = df1[cols].fillna(df1.mode().iloc[0])
df1.info()
df1.head(15)
df1[['house_direction', 'balcony_direction', 'toilet', 'bedroom', 'floor', 'nhà ngõ']].head(15)

#df1.drop(df1['nhà ngõ'].index, inplace= True)
#Lọc thông tin những bất động sản ở trong ngõ 
df1['nhà ngõ'] = df1['title'].str.contains('ngõ', case=False, na=False)
# Tạo  thành bộ dữ liệu nhà ngõ
df_ngo = df1[df1['nhà ngõ'] == True]
df_ngo.info()

# Tính toán giá/m2  ( đơn vị triệu/m2) với loại hình nhà ngõ
df_ngo['trieu/m2'] = df_ngo['price']/df_ngo['area']

df_ngo[['title', 'area', 'price', 'nhà ngõ', 'trieu/m2']].head(25)

# Phát hiện giá trị ngoại lai của các thuộc tính: diện tích, giá/m2 bằng phương pháp IQR
sns.boxplot(x=df_ngo['area'])
sns.boxplot(x=df_ngo['price'])
plt.show()

fig, ax = plt.subplots(figsize=(16,8))
ax.scatter(df_ngo['area'], df_ngo['price'])
ax.set_xlabel('Area')
ax.set_ylabel('Price')
plt.show()

z_score = stats.zscore(df_ngo)

df_ngo_dt_gia = df_ngo[['area', 'price']]

Q1 = df_ngo_dt_gia.quantile(0.25)
Q3 = df_ngo_dt_gia.quantile(0.75)
IQR = Q3 - Q1
print(IQR)

# lọc dữ liệu ngoại lai
df_ngo_dt_gia_moi = df_ngo_dt_gia[~((df_ngo_dt_gia<(Q1 - 1.5*IQR)) | (df_ngo_dt_gia > (Q3 + 1.5*IQR))).any(axis=1)]

df_ngo_dt_gia_moi.boxplot()
plt.show()

df_ngo_dt_gia.info()

fig, ax = plt.subplots(figsize=(16,8))
ax.scatter(df_ngo_dt_gia_moi['area'], df_ngo_dt_gia_moi['price'])
ax.set_xlabel('Area')
ax.set_ylabel('Price')
plt.show()

sns.boxplot(df_ngo_dt_gia_moi['area'])
plt.show()

# Chuẩn hóa dữ liệu bằng min-max scaling
scaler = MinMaxScaler()

df_ngo_minmax = df_ngo[['area', 'price', 'trieu/m2']]
# Chuẩn hóa dữ liệu trong df_ngo với StandardScaler
df_ngo_s = scaler.fit_transform(df_ngo_minmax)

col_names = list(df_ngo_minmax.columns)
df_ngo_s = pd.DataFrame(df_ngo_s, columns=col_names)

df_ngo_minmax.head(15)

