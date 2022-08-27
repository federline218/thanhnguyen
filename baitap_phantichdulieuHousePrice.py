from cmath import nan
import pandas as pd
import numpy as np

df = pd.read_excel('E:\PTDL\Pandas\house_price_dống-da.xlsx')
df.head()
df.shape
df.info()

#Lọc ra các bản ghi bán nhà riêng tại phường Trung liệt hoặc phường Khâm Thiên
df[(df['ward_name'] == 'Phường Trung Liệt') | (df['ward_name'] == 'Phường Khâm Thiên')] 

#Lọc các thông tin Địa chỉ, Giá, Hướng nhà, Hướng ban công của các bản ghi có giấy chứng nhận sổ đỏ và có 3 phòng ngủ trở lên.
df[(df['land_certificate'] == 'Sổ đỏ') & (df['bedroom']>=3)].filter(['address', 'price', 'house_direction', 'balcony_direction', 'land_certificate', 'bedroom']).count()


#Với mỗi loại nhà đất, tính trung bình cộng giá cũng như giá lớn nhất và giá nhỏ nhất.
df['type_of_land'] = df['type_of_land'].str.strip() # xóa khoảng trắng trong cột 'type_of_land'
df.pivot_table(values='price', index='type_of_land', aggfunc={'min','max', 'mean'})

df.info()
#Tính trung bình cộng số phòng ngủ, số phòng vệ sinh, số tầng của mỗi phường.
df.pivot_table(values=['bedroom', 'toilet', 'floor'], index='ward_name', aggfunc='mean')
