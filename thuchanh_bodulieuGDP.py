import pandas as pd
import numpy as np

df = pd.read_csv('E:\PTDL\GDPlist.csv', encoding = "ISO-8859-1")
print(df.shape)
print(df.info())

# doi ten cot 
df.rename(columns={'Country':'Nuoc', 'Continent':'Chauluc', 'GDP (millions of US$)':'GDP (trieu $)'}, inplace=True)
df

# df.drop(['Thanhpho'], axis=1, inplace=True)

# chen them cot
df.insert(1, 'Thanhpho', df.loc[:,'Nuoc']) 
df

# Trong cột Thanhpho, thay giá trị Vietnam thành Hanoi
df['Thanhpho'] = df['Thanhpho'].str.replace('Vietnam', 'Hanoi')
df

# Xóa các bản ghi có Chauluc là ‘Asia’
df = df.drop(df.loc[df['Chauluc'] == 'Asia'].index)
df

# Xóa các bản ghi có GDP < 300000
df = df.drop(df.loc[df['GDP (trieu $)'] < 300000].index)
df