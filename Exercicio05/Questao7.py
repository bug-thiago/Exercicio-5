notas = []
n = []
media = []
	q = 0

	print("Forneça as notas: ")

	for c in range(40):

		notas.append(float(input()))

	for c in range(0,40,4):

		n += [notas[c:c + 4]]

	for c in range(10):

		media += [sum(n[c]) / 4]

	for c in range(10):

		if media[c] >= 7:

			q += 1

	if q != 0:

		if q > 1:

			print("%d alunos têm média maior ou igual a 7.")

		else:

			print("%d aluno tem média maior ou igual a 7.")

	else:

		print("Nenhum aluno tem média maior ou igual a 7.")

#