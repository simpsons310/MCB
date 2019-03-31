
import math

def compute(a,b,opr):
	if opr == "add":
		return a+b
	if opr == "min":
		return a-b
	if opr == "mul":
		return a*b
	if opr == "div":
		return a/b
	if opr == "mod":
		return a%b
#a = int(input("Nhap so a: "))
#b = int(input("Nhap so b: "))
#opr = input("Nhap toan tu: ")
#kq = compute(a,b,opr)
#print( "ket qua ",kq)

def sortA(a,c,length):
	temp = 0
	for i in range(0,length-1):
		for j in range(i+1,length):
			if c == "asc":
				if(a[i] > a[j]):
					temp = a[i]
					a[i] = a[j]
					a[j] = temp
			elif c == "desc":
				if(a[i] < a[j]):
					temp = a[i]
					a[i] = a[j]
					a[j] = temp


#c = input("Chieu sap xep ")
#e =int(input ("phan tu mang "))
#d = []
#for i in range(0,e):
#	d.append(int(input("phan tu thu %d: "%(i+1))))
#sortA(d,c,e)
#print("Mang A:")
#print(d)

def sortM(a,c,m,n):
	k = 0
	b = []
	for i in range(0,m):
		for j in range(0,n):
			b.append(a[i][j])
			k = k + 1
	sortA(b,c,m*n)
	k = 0
	for i in range(0,len(a)):
		for j in range(0,len(a[i])):
			a[i][j] = b[k]
			k = k + 1	

#a = []
#m = int(input("Nhap so hang: "))
#n = int(input("Nhap so cot: "))
#for i in range(0,m):
#	a.append([])
#	for j in range(0,n):
#		a[i].append(int(input("a[%d][%d] = " %(i,j))))		
#c = input("Nhap cach sap xep: ")	
#sortM(a,c,m,n)
#print(a)	
	

def findV(a,cd,length):
	val = a[0]
	for i in range (0,length):
		if cd == "maximum":
			if val < a[i]:
				val = a[i]
		elif cd == "minimum":
			if val > a[i]:
				val = a[i]
	return val

#ar = []
#l = int(input("So phan tu: "))
#cd = input("Kieu tim: ")
#for i in range (0,l):
#	ar.append(int(input("Phan tu thu %d: "%(i+1))))
#val = findV(ar,cd,l)
#print(ar)
#print(val)

def decimal2binary(a):
	re = []
	s = ""
	count = 0
	while a != 0:
		temp  = int(a%2)
		a = int(a/2)
		re.append(temp)
		count = count + 1
	for i in range(0,count):
		st = str(re[i])
		s = st + s
	return s

#de = int(input("Nhap so thap phan: "))
#bi = decimal2binary(de)
#print(bi)

def binary2decimal(s):
	st = str(s)
	de = 0
	for i in range(0,len(st)):
		if st[i] == "0":
			base = 0
		elif st[i] == "1":
			base = 1
		de = de + pow(2,len(st)-i-1)*base
	return de

#bi = input("Nhap so nhi phan: ")
#kq = binary2decimal(bi)
#print(kq)


