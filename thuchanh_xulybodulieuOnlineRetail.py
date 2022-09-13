import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder

df = pd.read_csv("OnlineRetail.csv", encoding = "ISO-8859-1")
df.shape
df.head()
df.info()

# kiểm tra dữ liệu bị khuyết
df.isna()

# kiểm tra dữ liệu không bị khuyết
df['CustomerID'].notna()

# in những dòng ngoại lai Quantity < 0
df[df['Quantity'] < 0]

# #Xóa bỏ dòng ngoại lai của Quantity
df = df[df['Quantity']>=0]

# xóa những dòng chứa giá trị bị khuyết
df1 = df.dropna()
df1.shape

# xóa những dòng chứa toàn giá trị khuyết
df2 = df1.dropna(how='all')
df2.shape

# giữ những dòng có ít nhất 7 giá trị không bị khuyết
df3 = df.dropna(thresh=7)
df3.shape

# xóa những hàng mà có giá trị bị khuyết trên cột CustomerID
df4 = df.dropna(subset=['CustomerID'])
df4.shape

# thay thế những giá trị bị khuyết trên cột CustomerID bằng giá trị -1
df5 = df
df5['CustomerID'] = df5['CustomerID'].fillna(-1)

# hiển thị những dòng có CustomerID = -1 vừa được thay thế
df5[df5['CustomerID'] == -1]

# thay thế các giá trị bị khuyết ở cột Country bằng giá trị trước nó
df5['Country'] = df5['Country'].fillna(method='ffill')

#Xử lý dữ liệu ngoại lai
# vẽ box plot cho dữ liệu ở cột Quantity
sns.boxplot(x=df1['Quantity'])
plt.show()

# Xóa dữ liệu ngoại lai bằng IQR score
Q1 = df1['Quantity'].quantile(0.25)
Q3 = df1['Quantity'].quantile(0.75)
IQR = Q3 - Q1

# xác định phần tử không phải ngoại lai
df6 = df1
df6['outlier'] = ~((df1['Quantity'] < (Q1 - 1.5*IQR)) | (df1['Quantity'] > (Q3 + 1.5*IQR)))

# xóa phần tử ngoại lai
df6 = df6[df6['outlier'] == True]

# vẽ box plot cho dữ liệu ở cột Quantity
sns.boxplot(x=df6['Quantity'])
plt.show()

# vẽ biểu đồ hộp cho cột Quantity
sns.boxplot(x=df1['Quantity'])
plt.show()

# mô tả dữ liệu
df1['Quantity'].describe()

# chuẩn hóa dữ liệu với minmax scaling
scaler = MinMaxScaler()

# Chuẩn hóa dữ liệu trong df với MinMaxScaler ở 2 cột Quantity và UnitPrice
df_s = scaler.fit_transform(df1[['Quantity']])

# mô tả dữ liệu sau chuẩn hóa
pd.DataFrame(df_s).describe()

# vẽ lại biểu đồ hộp
sns.boxplot(df_s)
plt.show()

# chuẩn hóa dữ liệu với z-score scaling
scaler = StandardScaler()

# Chuẩn hóa dữ liệu trong df với StandardScaler ở 2 cột Quantity và UnitPrice
df_s = scaler.fit_transform(df1[['Quantity']])

# mô tả dữ liệu sau chuẩn hóa
pd.DataFrame(df_s).describe()

sns.boxplot(df_s)
plt.show()

sns.kdeplot(data=df_s)
plt.show()

# các giá trị ở cột Country
df1['Country'].unique()

# mã hóa cột Country với One-hot encoder sử dụng scikit learn
encoder = OneHotEncoder()

encoded_data = encoder.fit_transform(np.asarray(df1['Country']).reshape(-1,1))
encoded_data.todense()

# mã hóa cột Country với One-hot encoder sử dụng pandas
pd.get_dummies(df1['Country'])

# mã hóa cột Country với Label encoder sử dụng scikit learn
encoder = LabelEncoder()

encoded_data = encoder.fit_transform(np.asarray(df1['Country']))
encoded_data

# mã hóa cột Country với Label encoder sử dụng pandas
df1['Country'].astype('category').cat.codes

#Rời rạc hóa dữ liệu
# Rời rạc hóa dữ liệu ở cột UnitPrice

# chia thành 4 khoảng giá trị có độ dài bằng nhau
cats = pd.cut(df1['UnitPrice'], 4)
cats

# số lượng phần từ ở mỗi phần
pd.value_counts(cats)

# chia thành 4 phần có số lượng phần tử tương đương nhau
cats = pd.qcut(df1['UnitPrice'], 4)
cats

# số lượng phần từ ở mỗi phần
pd.value_counts(cats)