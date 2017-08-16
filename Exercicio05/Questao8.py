l = []
	m = 1

	print("Digite os números:")

	for c in range(5):

		l.append(int(input()))

	print("Soma: %d" % sum(l));

	for c in range(5):

		m *= l[c]

	if l[0] == 0 or l[1] == 0 or l[2] == 0 or l[3] == 0 or l[4] == 0:

		print("Multiplicação: 0")
		
	else:	

		print("Multiplicação: %d" % m)

	print("Números: ", end = "")

	for c in range(4):

		print("%d" % l[c], end = ", ")

	print("%d" % l[4])
