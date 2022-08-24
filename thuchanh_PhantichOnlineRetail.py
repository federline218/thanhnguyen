import pandas as pd
import numpy as np

df = pd.read_csv('E:\PTDL\OnlineRetail.csv', encoding = "ISO-8859-1")
df.head()
df.shape
df.info()
df.describe()

# với mỗi Số hóa đơn tính trung bình cộng số lượng các mặt hàng theo từng Quốc gia. 
df.pivot_table(values=['Quantity'], index= 'InvoiceNo', columns='Country', aggfunc={'Quantity': np.mean})

#với mỗi Khách hàng cho biết số lượng mua hàng lớn nhất và nhỏ nhất theo Kho.
df.pivot_table(values=['Quantity'] , index= 'CustomerID', columns='StockCode', aggfunc={min, max}).head(100)

# với mỗi Mã kho tính tổng số lượng các mặt hàng và trung bình cộng giá.
df.pivot_table(values=['Quantity', 'UnitPrice'], index='StockCode', aggfunc={'Quantity': np.sum, 'UnitPrice': np.mean})

#Xây dựng bảng Pivot table cho biết tổng số lượng hàng bán được của mỗi ngày.
df.pivot_table(values=['Quantity'], index= 'Description', columns='InvoiceDate', aggfunc={sum})