import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("E:\PTDL\OnlineRetail.csv", encoding = "ISO-8859-1")
df.head()
df.columns

# Lọc dữ liệu cần thiết cho mục tiêu 1.
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
d1 = df[['InvoiceNo', 'InvoiceDate']]
d1 = d1.drop_duplicates(subset = 'InvoiceNo', keep = 'first')
d1 = d1.set_index(['InvoiceDate'])
d2 = d1['2011']
d2 = d2.reset_index()
d3 = d2.groupby(by=d2['InvoiceDate'].dt.date).count()

# Vẽ biểu đồ đường.
x = d3.index.get_level_values(0)
plt.plot(x, d3['InvoiceDate'])
plt.title('Number of Invoices in 2011 (Daily)', fontsize = 16)
plt.xlabel('Date', fontsize = 14)
plt.ylabel('#Invoices', fontsize = 14)
plt.show()

# Lấy dữ liệu cần thiết cho mục tiêu 2: Vẽ biểu đồ cột so sánh số lượng đơn hàng trong các tháng của năm 2011.

d4 = d2.groupby(by=d2['InvoiceDate'].dt.month).count()
print(d4)

# Vẽ biểu đồ cột so sánh số lượng đơn hàng trong mỗi tháng năm 2011
x = d4.index.get_level_values(0)
plt.bar(x, d4['InvoiceDate'])
plt.title('Number of Invoices in 2011 (monthly)', fontsize = 16)
plt.xlabel('Month', fontsize = 14)
plt.ylabel('#Invoices', fontsize = 14)
plt.show()