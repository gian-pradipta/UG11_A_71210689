def hitung_hapus():
	a = input("Masukkan kalimat: ")
	b = int(input("Index Start :")) + 1
	c = int(input("Index Stop :")) + 1
	d = c - b + 1
	e = (d/len(a))*100
	
	if b > len(a) or c > len(a):
		return 0.0
	elif e < 0:
		return 0.0
	else:
		return e
	
print(hitung_hapus())