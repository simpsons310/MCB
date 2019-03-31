import giang as test

print("Test ham compute")
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
opr = input("Nhap toan tu (add,min,mul,div,mod): ")
kq = test.compute(a,b,opr)
print("Ket qua: %d"%kq)

print("")
print("Test ham sap xep mang")
e = int(input("So phan tu mang: "))
d = []
for i in range (0,e):
	d.append(int(input("Phan tu thu %d: "%(i+1))))
c = input("Chieu sap xep (asc,desc): ")
test.sortA(d,c,e)
print("Mang A: ")
print(d)

print("")
print("Test ham sap xep ma tran")
a = []
m = int(input("Nhap so hang: "))
n = int(input("Nhap so cot: "))
for i in range(0,m):
	a.append([])
	for j in range(0,n):
		a[i].append(int(input("a[%d][%d] = " %(i,j))))		
c = input("Nhap cach sap xep: ")	
test.sortM(a,c,m,n)
print(a)	


print("")
print("Test ham tim phan tu")
ar = []
l = int(input("So phan tu: "))
for i in range (0,l):
	ar.append(int(input("Phan tu thu %d: "%(i+1))))
cd = input("Kieu tim  (maximum,minimum): ")
val = test.findV(ar,cd,l)
print("Gia tri %s cua mang la: " %cd)
print(val)

print("")
print("Test ham chuyen doi so nhi phan sang thap phan")
de = int(input("Nhap so thap phan: "))
bi = test.decimal2binary(de)
print(bi)

print("")
print("Test ham chuyen doi so thap phan sang nhi phan")
bi = int(input("Nhap so nhi phan: "))
de = test.binary2decimal(bi)
print("ket qua: %d" %de)
