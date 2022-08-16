import pandas as pd
data = pd.read_csv('E:\PTDL\subset-covid-data.csv', encoding= 'UTF-8')
data.head()
data.info()
data.date.value_counts()

cleaned_data = data[data.date == '2020-04-12']
data.date.value_counts()

print('trung bình số ca mắc mới: ' + str(cleaned_data.cases.mean()))
print('trung vị của số ca mắc mới: ' + str(cleaned_data.cases.median()))
import matplotlib.pyplot as plt
plt.hist(cleaned_data.cases, bins = 200)
plt.title('Phân bổ số ca mắc mới')
plt.xlabel('số ca mắc mới')
plt.ylabel('số lượng quốc gia') 
plt.show()

print('tổng số ca nhiễm và số ca của các châu lục')