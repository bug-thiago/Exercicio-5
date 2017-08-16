	def lista(n):

		lista = []

		for c in range(1,n + 1):

			lista.append(c)

		return lista

	def mostraLista(lista):

		for c in range(len(lista)):

			print(lista[c], end = ".\n")

	n = int(input())
	print()
	mostraLista(lista(n))
