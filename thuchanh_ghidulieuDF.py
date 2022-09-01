import pandas as pd
df = pd.read_csv('E:\PTDL\FoodPrice_in_Turkey.csv') 
df.head()

#Ghi dữ liệu từ DataFrame vào file csv
df.to_csv('E:\PTDL\demo_FoodPrice.csv')

#Ghi dữ liệu từ DataFrame vào file excel
df.to_excel('E:\PTDL\demo_FoodPrice.xlsx')

#Ghi dữ liệu từ DataFrame vào file Json
df.to_json('E:\PTDL\demo_FoodPrice.json',orient='columns')

#Ghi dữ liệu từ DataFrame vào file HDF5
df.to_hdf('E:\PTDL\demo_FoodPrice.h5', 'table')

# Ghi dữ liệu từ DataFrame vào file HTML
df.to_html('E:\PTDL\demo_FoodPrice.html')



