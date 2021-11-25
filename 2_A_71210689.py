def ambil_tengah(x,y= None):
	if y == None:
		if len(x)%2 == 0:
			hasil = x[int(((len(x))/2))]
		else:
			hasil = x[int(((len(x) - 1)/2))]
		return hasil
	else:
		if len(x)%2 == 0:
			hasil = x[int(((len(x))/2) + y)]
		else:
			hasil = x[int(((len(x) - 1)/2) + y)]
		return hasil
	
print(ambil_tengah("abcdefg", 1))
print(ambil_tengah("abcdefg", 2))
print(ambil_tengah("abcd"))