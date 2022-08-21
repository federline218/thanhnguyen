import pandas as pd
import numpy as np
df = pd.read_csv('E:\PTDL\FoodPrice_in_Turkey.csv')

# Tính trung bình cộng giá của từng mặt hàng theo năm
df.pivot_table(values='Price', index='ProductName', columns='Year', aggfunc='mean')

# Tìm giá lớn nhất theo từng năm
df.pivot_table(values='Price', columns='Year', aggfunc='max')

#Tìm giá lớn nhất của từng mặt hàng
df.pivot_table(values='Price', index='ProductName', aggfunc='max')

#Tính giá lớn nhất, giá nhỏ nhất của từng địa điểm theo tháng
df1 = df.pivot_table(values='Price', columns='Place', index='Month', aggfunc={'min','max'})
df1.to_csv('E:\PTDL\FoodPrice_in_Turkey_new.csv') 

# Tính tổng giá và trung bình cộng số tháng bán hàng của từng mặt hàng theo địa điểm
df2 = df.pivot_table(values=['Price', 'Month'], index='ProductName', columns='Place', aggfunc={'Price':np.sum, 'Month':np.mean})
df2.to_csv('E:\PTDL\FoodPrice_in_Turkey_new2.csv') 
