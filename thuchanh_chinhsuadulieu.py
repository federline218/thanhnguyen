import pandas as pd

df = pd.read_csv('E:\PTDL\FoodPrice_in_Turkey.csv') 
df.head()

# Đổi tên cột thuộc tính
df.rename(columns={'Place':'Địa điểm', 'ProductName': 'Tên SP'}, inplace=True)
df.head()

# Thêm cột mới trong DataFrame với tất cả giá trị rỗng
df['new column'] = 'Nan'
df.head()

# Thêm cột giảm giá 10% cho tất cả các bản ghi
df['Giảm giá'] = pd.Series('10%', index= df.index)
df.head()

# Thêm cột giảm giá 12% cho tất cả các bản ghi
df.insert(10, 'Giảm giá 2', pd.Series('12%', index= df.index))
df.head()

# Thêm một dòng mới vào trong DataFrame
df = df.append({'Địa điểm':'NA', 'ProductId':'RR', 'Tên SP':'Rice','UmId':10,'UmName':'KG','Month':6,'Year':2021,'Price':84.3785,'Giảm giá':'10%','Giảm giá 2':'12%'}, ignore_index=True)
df.tail()

# Xóa một cột trong DataFrame
del df['new column']
df.head()

# Xóa một cột sử dụng phương thức pop()
df.pop('Giảm giá 2')

# Xóa một cột sử dụng phương thức drop() 
df.drop('Giảm giá', axis= 1, inplace=True)
df.head()

# Xóa nhiều cột sử dụng phương thức drop()
df.drop(['Month','Year'], axis=1, inplace=True)
df

# Xóa các dòng trong DataFrame
df.drop(1, axis=0, inplace=True)
df

# Xóa các dòng có chỉ số 7377 và 7379 sử dụng phương thức drop()
df.drop([7377, 7379], inplace= True)
df