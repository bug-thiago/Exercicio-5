a = []
	b = []
	 
	print("Digite os valores da primeira lista: ")
	 
	for c in range(10):
	 
	    a.append(float(input()))
	 
	print("Digite os valores da segunda lista: ")
	 
	for c in range(10):
	 
	    b.append(float(input()))
	 
	c = []
	 
	for x in range(10):
	 
	    c += [a[x]]
	    c += [b[x]]
