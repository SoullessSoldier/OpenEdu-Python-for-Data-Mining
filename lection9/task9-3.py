"""
По данным портала открытых данных Москвы определите количество дней, когда освещение включено 12 часов или более.
"""
"""
dataset 3288
https://data.mos.ru/opendata/3288
"""
from urllib.request import urlopen
import json

url="https://apidata.mos.ru/v1/datasets/3288/rows?api_key=c25290a0b5f170f69d45a28665b43168"
res=urlopen(url).read().decode('utf-8')
"""
fout=open('out9-3.txt','w',encoding='utf-8')
print(res,file=fout)
"""
cnt=0
lst=json.loads(res)
for now in lst:
    if int(now['Cells']['DurationOfLighting'][0:2])>11:
        cnt+=1
print(cnt)#164