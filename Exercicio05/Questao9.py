idade = []
	altura = []

	print("Digite as idades e as alturas, respectivamente:")

	for c in range(5):

		idade.append(int(input()))
		altura.append(float(input()))

	idadesInvertidas = idade[::-1]
	alturasInvertidas = altura[::-1]

	print("\nIdades: ", end = "")

	for c in range(4):

		print("%d" % idadesInvertidas[c], end = ", ")

	print(idadesInvertidas[4])

	print("Alturas: ", end = "")

	for c in range(4):

		print("%.2f" % alturasInvertidas[c], end = ", ")

	print("%.2f" % alturasInvertidas[4])