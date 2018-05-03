# -*- coding:utf-8 -*-
#V:Python 3.6.3
import pandas as pd
from wordcloud import WordCloud
from IPython.display import display
from matplotlib.pylab import plt

data = pd.read_csv('jobs.csv')
salary = data['low_salary']
salary2 = data['high_salary']
position = data['position']
print(salary,position)

plt.figure(figsize=(10,6))
plt.rc('font',family='SimHei',size=15)
plt.title(u'南京互联网工作的最低工资')
plt.xlabel(u'职位')
plt.ylabel(u'最低工资')
plt.bar(position,salary,color='g',width=2)
plt.show()


plt.figure(figsize=(10,6))
plt.rc('font',family='SimHei',size=15)
plt.title(u'南京互联网工作的最高工资')
plt.xlabel(u'职位')
plt.ylabel(u'最高工资')
plt.bar(position,salary2,color='r')
plt.show()