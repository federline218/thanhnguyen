from ctypes.wintypes import SHORT
import pandas as pd
data = pd.read_csv('E:\PTDL\OnlineRetail.csv', encoding = "ISO-8859-1")
data.head()
print(data.info())

country = data.Country.unique() 
print('So luong cac quoc gia: ' + str(country.size))

# Tao cot thanh tien cua cac mat hang
data['Total'] = data['Quantity'] * data['UnitPrice']  

# Gia tri don hang cua moi don hang
total_invoices = data['Total'].sum()
count_invoices = data.groupby('InvoiceNo')
print('So luong hoa don ban ra: ' + str(count_invoices.sum()))
print('Tong doanh thu: ' + str(total_invoices.sum())) 

# top 10 mat hang co so luong ban ra lon nhat
print('Top 10 mat hang co so luong ban ra lon nhat')
quantity_product = data.groupby(['StockCode','Description']).sum('Quantity')
quantity_product.sort_values('Quantity' , ascending = False).head(10)

#top 10 mat hang co doanh thu lon nhat
print('Top 10 mat hang co doanh thu lon nhat')
total_product = data.groupby(['StockCode','Description']).sum('Total')
total_product.sort_values('Total' , ascending = False).head(10)

