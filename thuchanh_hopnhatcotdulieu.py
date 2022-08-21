import pandas as pd
import numpy as np

df = pd.read_csv('E:\PTDL\FoodPrice_in_Turkey.csv')
df.info()

# Xóa các dòng có thuộc tính ProductID trùng nhau, giữ lại bản ghi cuối cùng, thiết lập lại chỉ số
df = df.drop_duplicates(['ProductId'], keep= 'last').reset_index(drop=True)
df

# Tách file chứa thông tin sản phẩm
df_pro = df.loc[:, ['ProductId', 'ProductName', 'UmId', 'UmName']]
df_pro

# Tách file chứa thông tin giá
df_pri = df.loc[:, ['ProductId', 'Place', 'Month','Year','Price']]
df_pri

# Tách file chứa thông tin giá với số dòng từ bản ghi 10 đến 20
df_pri10 = df.loc[10:20, ['ProductId', 'Place', 'Month','Year','Price']]
df_pri10

# Dùng phương thức merge ghép 2 dataFrame có cùng chung một cột thuộc tính
df1 = pd.merge(df_pro, df_pri, on= 'ProductId')
df1

# Dùng phương thức concat cho phép ghép từ hai dataFrame trở lên lại với nhau
df2 = pd.concat([df_pro, df_pri, df_pri10], axis= 1)
df2