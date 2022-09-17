import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("E:\PTDL\GDPlist.csv", encoding = "ISO-8859-1")
df.head()

# So sánh GDP các nước ở South America.
df1 = df[df['Continent'] == 'South America']
plt.bar(df1['Country'], df1['GDP (millions of US$)'])
plt.title('GDP of Countries in South America ', fontsize = 16)
plt.xlabel('Country', fontsize = 14)
plt.ylabel('GDP', fontsize = 14)
plt.show()

# Đánh giá tỉ lệ đóng góp GDP của Việt Nam trên tổng số GDP của 5 nước Đông Nam Á là Vietnam,  Indonesia, Cambodia, Thailand và Malaysia.
df['Country'] = df['Country'].str.strip() # xóa khoảng trắng ở đầu
DNA = df['Country'].isin(['Vietnam', 'Indonesia', 'Cambodia', 'Thailand', 'Malaysia'])
df[DNA]

plt.pie(df[DNA]['GDP (millions of US$)'], labels=df[DNA]['Country'],  autopct='%1.2f%%')
plt.title('GDP of VN vs DNA ', fontsize = 16)
plt.show()

