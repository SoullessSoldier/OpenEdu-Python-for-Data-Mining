'''
Напишите программу, которая будет разрезать большую прямоугольную область на N×N одинаковых прямоугольных областей.
Области задаются четырьмя координатами:
минимальной широтой, минимальной долготой, максимальной широтой, максимальной долготой.

При выводе области должны быть упорядочены по возрастанию минимальной широты,
а в случае равных широт - по возрастанию минимальной долготы.

Гарантируется, что все числа во входных данных положительны.

Sample Input:

41.173 77.23 42.17 79.004
2
Sample Output:

41.173 77.23 41.6715 78.117
41.173 78.117 41.6715 79.004
41.6715 77.23 42.17 78.117
41.6715 78.117 42.17 79.004
'''
coords=list(map(float,input().split()))
step=int(input())
minlat=coords[0]
minlon=coords[1]
maxlat=coords[2]
maxlon=coords[3]
dlat=(maxlat-minlat)/step#размер окна по широте
dlon=(maxlon-minlon)/step
l_map=[]
for i in range(step):
    for j in range(step):
        nminlat = minlat + dlat * i
        nmaxlat = minlat + dlat * (i + 1)
        nminlon = minlon + dlon * j
        nmaxlon = minlon + dlon * (j + 1)
        l_map.append([nminlat,nminlon,nmaxlat,nmaxlon])
for i in sorted(l_map,key=lambda x: (x[0],x[1])):
    print(*i)