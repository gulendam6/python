
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
 
sayi = int(input("Sayi Giriniz:"))
sayac=0 
toplam=0
sayac2=0
 
for i in range(2,(sayi+1)):
    sayac=0
    for j in range(2,i):
        if(i%j==0):
            sayac=sayac+1
            break
    if(sayac==0):
        print(i)
        sayac2=sayac2+1
        
print("Toplam ",sayac2," adet asal sayı var.")
 
