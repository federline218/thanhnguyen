import pandas as pd
import numpy as np

df = pd.read_csv('E:\PTDL\shopeep_koreantop_clothing_shop_data.csv')
df.head()

# Để đơn giản ta thực hiện lọc tập dữ liệu ban đầu theo các thuộc tính sau
df = df[['join_month', 'join_day','join_year','shop_location','rating_bad','rating_good','rating_normal']]
df

# Tạo cột 'rating' 
df['rating'] = df['rating_good']*2 + df['rating_normal'] - df['rating_bad']*3
df

# ghép 3 cột join_month, join_day, join_year thành cột mới có tên 'date' nhận giá trị có dạng: "join_month join_day,join_year"
df['date'] = df['join_month'] + ' ' + df['join_day'].astype(str) + ',' + df['join_year'].astype(str)
df

# Thêm cột new có giá trị True nếu join_year = 2021 và False trong trường hợp còn lại.
df['new'] = df['join_year'] == 2021
df

# Thêm cột rate có giá trị good nếu rating_good >= 50000,  bad trong trường hợp còn lại
df['rate'] = np.where(df['rating_good']>=50000, 'good', 'bad')
df

# Thêm cột flag tặng cờ cho các cửa hàng, flag nhận các giá trị như sau:
conditions = [(df['rating_good'] >= 30000) & (df['rating_bad'] <= 100),
              (df['rating_good'] >= 10000) & (df['rating_good'] < 30000) & (df['rating_bad'] <= 1000) & (df['rating_bad'] > 100),
              (df['rating_good'] < 10000)]
choices = ['blue', 'yellow', 'red']
df['flag'] = np.select(conditions, choices, default='black')
df.head(40)
df[['rating_good', 'rating_bad', 'flag']].head(50)

