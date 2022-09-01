import pandas as pd
import numpy as np
df=pd.read_csv('FoodPrice_in_Turkey.csv')

# Tách file 1 chứa 5000 bản ghi đầu tiên
df1 = df.loc[0:4999,:]
df1

# Tách file 2 chứa các bản ghi còn lại
df2 = df.loc[5000:7381,:]
df2

# Tách file 3 chứa thông tin giá với số dòng từ bản ghi 1000 đến 2000
df3 = df.loc[1000:2000, ['Price', 'Place','Month','Year','Price']]
df3

#Ghép các dòng từ các file
df4 = pd.concat([df1,df2], axis=0) #axis=0 du lieu dc ghep theo dong
df4

df5 = pd.concat([df1, df2, df3], axis= 0)
df5

df6 = df1.append(df2)
df6

df7 = df1.append(df3)
df7