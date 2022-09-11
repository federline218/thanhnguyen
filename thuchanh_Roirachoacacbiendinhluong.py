from unicodedata import name
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

# định nghĩa khoảng giá trị các nhóm
bins = [18, 25, 35, 60, 100]

# thực hiện rời rạc hóa
cats = pd.cut(ages, bins)
cats

# lấy ra index của nhóm tương ứng với các phần tử
cats.codes

# lấy ra các nhóm
cats.categories

# thống kê số lượng phần tử ở mỗi nhóm
pd.value_counts(cats)

#Chúng ta có thể thay đổi phía bị đóng bằng cách truyền vào tham số right = False:
pd.cut(ages, [18, 26, 36, 61, 100], right=False)

# danh sách nhãn
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']

pd.cut(ages, bins, labels=group_names)

# sinh dữ liệu ngẫu nhiên gồm 20 phần tử
data = np.random.rand(20)
#Tùy chọn precision = 2 sẽ giới hạn độ chính xác thập phân ở hai chữ số.
cut_data = pd.cut(data, 4, precision=2)
cut_data

pd.value_counts(cut_data)

 # sinh ngẫu nhiễn 1000 điểm dữ liệu
data_1 = np.random.randn(1000)
# thực hiện hàm qcut trên dữ liệu vừa sinh ra
catq = pd.qcut(data_1, 4)
catq
#thống kê số lượng phần tử
pd.value_counts(catq)

pd.qcut(data_1, [0, 0.1, 0.5, 0.9, 1.])