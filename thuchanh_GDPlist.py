import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('E:\PTDL\GDPlist.csv', encoding = "ISO-8859-1")

data.info()

print('Su dong deu GDP cua cac quoc gia')
plt.hist(data['GDP (millions of US$)'], bins=100)
plt.show()

# So quoc gia trong moi chau luc
print('So quoc gia trong moi chau luc:' )
count_country = data.groupby('Continent').count()
count_country

# Tong GDP cua cac chau luc
print('Tong GDP cua cac chau luc:' )
total_GDP = data.groupby('Continent').sum()
total_GDP

# Top 10 quoc gia co GDP cao nhat
print('10 quoc gia co GDP cao nhat: ')
data.sort_values(['GDP (millions of US$)'], ascending=False).head(10)




