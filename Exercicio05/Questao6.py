
	n = []

	print("Digite vinte números inteiros: ")

	for c in range(20):

		n.append(int(input()))

	PAR = []
	impar = []

	for c in range(20):

		if n[c] % 2 == 0:

			PAR.append(n[c])

		else:

			impar.append(n[c])

	print("\nNúmeros lidos: ", end = "")

	for c in range(19):

		print(n[c], end = ", ")

	print(n[19])

	print("Números pares: ", end = "")

	for c in range(len(PAR) - 1):

		print(PAR[c], end = ", ")

	print(PAR[len(PAR) - 1])

	print("Números ímpares: ", end = "")

	for c in range(len(impar) - 1):

		print(impar[c], end = ", ")

	print(impar[len(impar) - 1])