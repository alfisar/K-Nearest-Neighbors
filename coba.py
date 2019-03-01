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

def hitung(lis1,max,key,k):
    beda,j, = 0,0
    for row in lis1 :
        if (row[6] != lis3[j]) : 
            beda = beda + 1
        j = j + 1 
    jumlah = 320 - beda
    akurasi = (float(jumlah) / float(320)) * 100
    if(max <= akurasi):
        max = akurasi
        key = k
    return max,key,akurasi

def takeSecond1(elem):
    return elem[1]


f = open("DataTrain.csv","r")
reader = csv.reader(f)
next(reader)

max = 0
lis1 = []
lis2 = []
lis3 = []
lis4 = []
i,j,beda,temp0,temp1,temp2,temp3,key = 0,0,0,0,0,0,0,0

for d in reader :
    if (temp1 < 80 ) and (int(d[6]) == 1):
        lis1.append((d[0],d[1],d[2],d[3],d[4],d[5],int(d[6])))
        temp1 = temp1 + 1
    elif (temp2 < 80 ) and (int(d[6]) == 2):
        lis1.append((d[0],d[1],d[2],d[3],d[4],d[5],int(d[6])))
        temp2 = temp2 + 1
    elif (temp3 < 80 ) and (int(d[6]) == 3):
        lis1.append((d[0],d[1],d[2],d[3],d[4],d[5],int(d[6])))
        temp3 = temp3 + 1
    elif (temp0 < 80 ) and (int(d[6]) == 0):
        lis1.append((d[0],d[1],d[2],d[3],d[4],d[5],int(d[6])))
        temp0 = temp0 + 1
    else :
        lis4.append((d[0],d[1],d[2],d[3],d[4],d[5],int(d[6])))


for k in range(1,201):
    lis3 = []
    for row in lis1 :
        for roww in lis4 :
            hasil = jarak(float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(roww[1]),float(roww[2]),float(roww[3]),float(roww[4]),float(roww[5]))
            lis2.append((roww[0],hasil,roww[6]))
        lis2.sort(key=takeSecond1)
        hasil2 = pemilihan(lis2)
        lis3.append(hasil2) 
        lis2 = []
    max,key,akurasi = hitung(lis1,max,key,k)
    print(i,key)
    print(akurasi)
    i = i + 1
print('K optimum : ',key)
print('Akurasi : ',max)