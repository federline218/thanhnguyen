import pandas as pd
import numpy as np



df = pd.read_csv('E:\PTDL\OnlineRetail.csv', encoding = "ISO-8859-1")
print(df.shape)
df.info()
df.head()

#Trích xuất dữ liệu các cột Description và Quantity lưu vào file OnlineRetail.csv

df1 = df.loc[:,['Description','Quantity']] # Truy cap den 2 cot Description va Quantity
df1.to_csv('E:\PTDL\OnlineRetail_new.csv')

# Trích xuất dữ liệu 1000 dòng đầu tiên lưu vào file OnlineRetail.xlsx
df2 = df.head(1000)
df2.to_excel('E:\PTDL\OnlineRetail_new.xlsx')

# Trích xuất các bản ghi có số lượng từ 10 trở lên lưu vào file OnlineRetail.h5
df3 = df.loc[df['Quantity'] > 10]
df3.to_hdf('E:\PTDL\OnlineRetail_new.h5', 'table')

# Trích xuất dữ liệu các phần tử từ dòng 1000 đến dòng 2000, các cột Quantity, InvoiceDate, UnitPrice lưu vào file OnlineRetail.json
df4 = df.iloc[1000:2000]
df4 = df4.loc[:,['Quantity', 'InvoiceDate', 'UnitPrice']]
df4.to_json('E:\PTDL\OnlineRetail.json',orient='columns')

# Trích xuất các bản ghi có số hóa đơn ‘536365’ lưu vào file OnlineRetail.html
df5 = df.loc[df['InvoiceNo'] == '536365']
df5.to_html('E:\PTDL\OnlineRetail.html')