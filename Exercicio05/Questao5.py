x = []
consoantes = []

	for c in range(10):

		x.append(input())

	cons = 0

	for c in range(10):

		if x[c] != "a" and x[c] != "e" and x[c] != "i" and x[c] != "o" and x[c] != "u":

			consoantes.append(x[c])
			cons += 1

	print("\n\n%d Consoantes:" % (cons), end = " ")

	for c in range(len(consoantes) - 1):

		print(consoantes[c], end = ", ")

	print(consoantes[len(consoantes) - 1])