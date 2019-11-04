"""
10.3 matplotlib: круговые диаграммы
https://eax.me/python-matplotlib/

"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import csv

data_names = ['Москва', 'Санкт-Петербург', 'Сочи', 'Архангельск',
              'Владимир', 'Краснодар', 'Курск', 'Воронеж',
              'Ставрополь', 'Мурманск']
data_values = [1076, 979, 222, 189, 137, 134, 124, 124, 91, 79]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 9})

plt.title('Распределение кафе по городам России (%)')

xs = range(len(data_names))

plt.pie(
    data_values, autopct='%.1f', radius = 1.1,
    explode = [0.15] + [0 for _ in range(len(data_names) - 1)] )
#autopct - количество знаков после запятой в данных
#explode - насколько долька должна уехать относительно других, тут реализовано через итератор
plt.legend(
    bbox_to_anchor = (-0.16, 0.45, 0.25, 0.25),
    loc = 'lower left', labels = data_names )
plt.show()
#fig.savefig('pie.png')