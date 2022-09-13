import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder

data = pd.read_csv('E:\PTDL\FoodPrice_in_Turkey.csv') 
data.head()
data.shape
# mô tả dữ liệu
data.describe().T
# thông tin dữ liệu
data.info()
# kiểm tra dữ liệu bị khuyết
data.isna()
# xóa những dòng chứa giá trị bị khuyết
df1 = data.dropna()
df1.shape

# Xử lý dữ liệu ngoại lai cho đặc trưng Price
sns.boxplot(x=df1['Price'])
plt.show()

# Xóa dữ liệu ngoại lai bằng IQR score
Q1 = df1['Price'].quantile(0.25)
Q3= df1['Price'].quantile(0.75)
IQR = Q3 - Q1

# xác định phần tử không phải ngoại lai
df2 = df1
df2['outlier'] = ~((df1['Price'] < (Q1 - 1.5*IQR)) | (df1['Price'] > (Q3 + 1.5*IQR)))

# xóa phần tử ngoại lai
df2 = df2[df2['outlier'] == True]

sns.boxplot(x=df2['Price'])
plt.show()

df2['Price'].describe()

# biểu đồ phân bố dữ liệu
sns.kdeplot(data=df2['Price'])  
plt.show()

# chuẩn hóa dữ liệu với minmax scaling
scaler = MinMaxScaler()
df_s = scaler.fit_transform(df2[['Price']])

# mô tả dữ liệu sau chuẩn hóa
pd.DataFrame(df_s).describe()

# vẽ lại biểu đồ hộp
sns.boxplot(x=df_s)
plt.show()

# biểu đồ phân bố dữ liệu
sns.kdeplot(data=df_s)
plt.show()

# các giá trị ở cột ProductName
df2['ProductName'].unique()

# mã hóa cột ProductName với One-hot encoder sử dụng scikit learn
encoder = OneHotEncoder()

encoded_data = encoder.fit_transform(np.asarray(df2['ProductName']).reshape(-1,1))
encoded_data.todense()

# mã hóa cột ProductName với One-hot encoder sử dụng pandas
pd.get_dummies(df2['ProductName'])

# mã hóa cột ProductName với Label encoder sử dụng scikit learn
encoder_LB = LabelEncoder()

encoded_data_LB = encoder_LB.fit_transform(np.asarray(df2['ProductName']))
encoded_data_LB

# mã hóa cột ProductName với Label encoder sử dụng pandas
df2['ProductName'].astype('category').cat.codes

# Rời rạc hóa dữ liệu
# Rời rạc hóa dữ liệu ở cột Price
# chia thành 5 khoảng giá trị có độ dài bằng nhau
cats = pd.cut(df2['Price'], 5)
cats

# số lượng phần từ ở mỗi phần
pd.value_counts(cats)

# chia thành 5 phần có số lượng phần tử tương đương nhau
cats_equal = pd.qcut(df2['Price'], 5)
cats_equal
pd.value_counts(cats_equal)

