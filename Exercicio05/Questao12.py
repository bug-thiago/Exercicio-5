a = []
	b = []
	c = []
	 
	print("Digite os valores da primeira lista: ")
	 
	for i in range(10):
	 
	    a.append(float(input()))
	 
	print("Digite os valores da segunda lista: ")
	 
	for i in range(10):
	 
	    b.append(float(input()))
	 
	print("Digite os valores da terceira lista: ")
	 
	for i in range(10):
	 
	    c.append(float(input()))
	 
	d = []
	 
	for x in range(10):
	 
	    d += [a[x]]
	    d += [b[x]]
	    d += [c[x]]