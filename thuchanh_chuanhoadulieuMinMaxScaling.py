import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# tạo các cột theo các phần phối khác nhau
df = pd.DataFrame({ 
    'beta': np.random.beta(5, 1, 1000) * 60,        # beta
    'exponential': np.random.exponential(10, 1000), # exponential
    'normal_p': np.random.normal(10, 2, 1000),      # normal platykurtic
    'normal_l': np.random.normal(10, 10, 1000),     # normal leptokurtic
})

df.head()

# thêm dữ liệu được tạo theo phân phối nhị thức
first_half = np.random.normal(20, 3, 500) 
second_half = np.random.normal(-20, 3, 500) 
bimodal = np.concatenate([first_half, second_half])

df['bimodal'] = bimodal

# Trực quan hóa dữ liệu sinh ra
sns.kdeplot(data=df)
plt.show()

#Hiển thị thống kê
df.describe()

#Thêm một đặc trưng với giá trị lớn hơn nhiều
normal_big = np.random.normal(1000000, 10000, (1000,1))  # normal distribution of large values
df['normal_big'] = normal_big
sns.kdeplot(data=df)
plt.show()

# trực quan hóa bằng biểu đồ box plot
df.boxplot()
plt.show()

#Chuẩn hóa với Min-Max scaling
# Khai báo đối tượng MinMaxScaler
scaler = MinMaxScaler()

# Chuẩn hóa dữ liệu trong df với StandardScaler
df_s = scaler.fit_transform(df)

# lấy danh sáchc cột
col_names = list(df.columns)

# chuyển về DataFrame, gán các cột của df cho dữ liệu đã được chuẩn hóa
df_s = pd.DataFrame(df_s, columns=col_names)

df_s.head()

# biểu diễn dữ liệu đã được chuẩn hóa
sns.kdeplot(data=df_s)
plt.show()

# trực quan hóa bằng biểu đồ box plot
df_s.boxplot()
plt.show()

# thống kê về dữ liệu được sinh ra
df_s.describe()

# lấy giá trị min của cột beta
df_s['beta'].min()

# lấy giá trị max của cột beta
df_s['beta'].max()

# in các giá trị min của từng cột trong dữ liệu chưa chuẩn hóa
mins = [df[col].min() for col in df.columns]
mins

# in các giá trị min của từng cột trong dữ liệu đã chuẩn hóa
minsCH = [df_s[col].min() for col in df.columns]
minsCH

# in các giá trị max của từng cột dữ liệu chưa chuẩn hóa
maxs = [df[col].max() for col in df.columns]
maxs

# in các giá trị max của từng cột dữ liệu đã chuẩn hóa
maxCH = [df_s[col].max() for col in df_s.columns]
maxCH