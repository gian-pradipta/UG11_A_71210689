
def calculator():
	return("======== Calculator sederhana ========\n1. Pertambahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Pangkat")

def tambah():
	b = float(input("Masukkan bilangan 1: "))
	c = float(input("Masukkan bilangan 2: "))
	return b + c
def kurang():
	b = float(input("Masukkan bilangan 1: "))
	c = float(input("Masukkan bilangan 2: "))
	return b - c
def bagi():
	b = float(input("Masukkan bilangan 1: "))
	c = float(input("Masukkan bilangan 2: "))
	return b/c
def kali():
	b = float(input("Masukkan bilangan 1: "))
	c = float(input("Masukkan bilangan 2: "))
	return b*c

def pangkat():
	b = float(input("Masukkan bilangan 1: "))
	c = float(input("Masukkan bilangan 2: "))
	return b**c

print(calculator())
a = int(input("Masukkan pilihan: "))
if a == 1:
	x= tambah()
	print("Hasilnya: ", x)
elif a == 2:
	x = kurang()
	print("Hasilnya: ", x)
elif a == 3:
	x = kali()
	print("Hasilnya: ", x)
elif a == 4:
	x = bagi()
	print("Hasilnya: ", x)
elif a == 5:
	x = pangkat()
	print("Hasilnya: ", x)
else:
	print("Maaf, input operasi antara 1-5")
		