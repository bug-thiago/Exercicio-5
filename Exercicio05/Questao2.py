def cincoInteiros(a, b, c, d, e):

		return [a, b, c, d, e]

	def mostraLista(lista):

		print()

		for c in range(len(lista) - 1):

			print(lista[c], end = ", ")

		print(lista[len(lista) - 1])

	try:

		mostraLista(cincoInteiros(int(input()), int(input()), int(input()), int(input()), int(input())))

	except:

		print("Não foram digitados valores inteiros.")
