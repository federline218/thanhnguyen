import pandas as pd

#đọc dữ liệu từ file csv
df = pd.read_csv('E:\PTDL\FoodPrice_in_Turkey.csv') 
df.head()

#đọc dữ liệu từ file excel
df = pd.read_excel('E:\PTDL\Pandas\house_price_dống-da.xlsx')
df.head()

#đọc dữ liệu từ file Json
df = pd.read_json('FoodPrice.json')
df.head()

#Đọc dữ liệu từ file hdf5
df=pd.read_hdf('FoodPrice.h5', 'table')
df.head()

#Đọc dữ liệu từ file html
url = 'https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_North_America'
df = pd.read_html(url)
df[0].head()
