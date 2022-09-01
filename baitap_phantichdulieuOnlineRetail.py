from distutils.log import error
import pandas as pd
import numpy as np

df = pd.read_csv('E:\PTDL\OnlineRetail.csv', encoding='ISO-8859-1') 
df.head()
df.shape
df.info()

# df= df.drop(['Month','Day'], axis=1)
# Tach ngay gio
df['Day'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M').dt.day
df['Month'] = pd.to_datetime(df['InvoiceDate'], format= '%m/%d/%Y %H:%M').dt.month
df['Year'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M').dt.year
df['Hour'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M').dt.hour
df['Minute'] = pd.to_datetime(df['InvoiceDate'], format='%m/%d/%Y %H:%M').dt.minute


df.head(15)

#Tạo cột mới có tên quý –  ‘Previous’ nhận giá trị 1 nếu ngày lập hóa đơn nằm trong các tháng 1,2,3; nhận giá trị 2 nếu ngày lập hóa đơn nằm trong các tháng 4,5,6; nhận giá trị 3 nếu ngày lập hóa đơn nằm trong các tháng 7,8,9;  nhận giá trị 4 nếu ngày lập hóa đơn nằm trong các tháng 10,11,12;

conditions = [(df['Month']<=3), (df['Month']>3) & (df['Month']<=6), (df['Month']>6) & (df['Month']<=9), (df['Month']>9) & (df['Month']<=12)]
choices = [1,2,3,4]

df['Previous'] = np.select(conditions, choices)
df[['InvoiceNo', 'Month', 'Previous']].iloc[185552:185652]

# Tạo một cột mới có tên ‘Amount’ có giá trị bằng Quantity * UnitPrice
df['Amount'] = df['Quantity']*df['UnitPrice']
df[['InvoiceNo', 'Quantity', 'UnitPrice', 'Amount']].iloc[25:78]

#Tạo cột mới ‘Discount’ nhận giá trị 10% nếu Country là ‘United Kingdom’ và thuộc quý 4, 5% nếu là ‘France’ ngược lại là 0%
conditions2 = [(df['Country']=='United Kingdom') & (df['Previous'] == 4), (df['Country']=='France')]
choices2 = ['10%' , '5%'] # '{0:.0%}'.format(10/100) , '{0:.0%}'.format(5/100)

df['Discount'] = np.select(conditions2, choices2, default='0%')
df[['Country','Amount', 'Previous', 'Discount']].iloc[28:78]

#Tạo cột mới ‘Total’ nhận giá trị bằng: Amount – Discount.
df.info()
# df['Discount'] = df['Discount'].astype(float)
# df['Discount'] = pd.to_numeric(df['Discount'], errors= 'coerce')
df['Discount'].str.rstrip('%').astype(float) # vì cột 'Discount' có kiểu object nên phải xử lý cắt ký tự '%' sau đó convert sang kiểu float
df['Total'] = df['Discount'] * df['Amount']/100
df[['Country','Amount', 'Previous', 'Discount', 'Total']].iloc[28:78]


# pd.to_numeric(df['Discount'], error= 'coerce')

