import numpy
import csv
import math

def jarak(v1,w1,x1,y1,z1,v2,w2,x2,y2,z2):
    distance = ((v2-v1)**2) + ((w2-w1)**2) + ((x2-x1)**2) + ((y2-y1)**2) + ((z2-z1)**2)
    return math.sqrt(distance)

def pemilihan(x):
    nol,satu,dua,tiga = 0,0,0,0
    temp = []
    for h in range(k) :
        if (x[h][2] == 0 ):
            nol = nol + 1
        elif (x[h][2] == 1 ) :
            satu = satu + 1
        elif (x[h][2] == 2 ) :
            dua = dua + 1
        elif (x[h][2] == 3 ) :
            tiga = tiga + 1 
    
    temp.append((0,nol))
    temp.append((1,satu))
    temp.append((2,dua))
    temp.append((3,tiga))
    temp.sort(key=takeSecond1)
    return temp[3][0]
    
def takeSecond1(elem):
    return elem[1]


f = open("DataTrain.csv","r")
reader = csv.reader(f)
next(reader)

f1= open("DataTest.csv","r")
reader1 = csv.reader(f1)
next(reader1)

g = open("TebakanTugas3.csv","w")
w = csv.writer(g)
w.writerow(("Y"))

k = 14
lis1 = []
lis2 = []
lis3 = []
lis4 = []
i,j,beda = 1,0,0

for d in reader :
    lis1.append((d[0],d[1],d[2],d[3],d[4],d[5],int(d[6])))

for d1 in reader1 :
    lis2.append((d1[0],d1[1],d1[2],d1[3],d1[4],d1[5]))


for row in lis2 :
    for roww in lis1 :
        hasil = jarak(float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(roww[1]),float(roww[2]),float(roww[3]),float(roww[4]),float(roww[5]))
        lis3.append((roww[0],hasil,roww[6]))
    lis3.sort(key=takeSecond1)
    hasil2 = pemilihan(lis3)
    w.writerow((str(hasil2)))
    print(hasil2)
    lis3 = []
    i = i + 1 
f.close()
f1.close()
g.close()