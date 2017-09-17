def back():
	a=input("enter a string")
	for i in list(range(len(a))):
		print(a[len(a)-1-i])
back()