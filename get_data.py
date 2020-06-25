#做图，整体看走向
import pandas as pd
from pylab import *
mpl.rcParams['font.sans-serif']=['SimHei']


data=pd.read_excel('./huaxia.xlsx',skiprows=111,header=None)#忽略0-111索引行
print(data.head())
data1=pd.read_excel('./pufa.xlsx',skiprows=111,header=None)#忽略0-111索引行
print(data1.head())
data2=pd.read_excel('./tongrentang.xlsx',skiprows=111,header=None)#忽略0-111索引行
print(data2.head())
plt.plot(data[0],data[1],label='华夏银行')
plt.plot(data1[0],data1[1],label='浦发银行')
plt.plot(data2[0],data2[1],label='同仁堂')
plt.legend()
plt.xlabel('时间')
plt.ylabel('开盘价')
plt.savefig('./stocks.png')
plt.show()
