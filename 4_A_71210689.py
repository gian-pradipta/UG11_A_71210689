def ambildanbalik(a,b,c,d):
	if d == False:
		e = a[b-1:c]
	else:
		e = a[c-1:b-2:-1]
	return e
	
print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("qwerty",3,4,True))
print(ambildanbalik("qwerty",2,2,False))