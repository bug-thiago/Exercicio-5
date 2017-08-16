idade = []
	altura = []
	x = 0

	print("Digite as idades e as alturas, respectivamente, de cada um dos alunos: ")

	for c in range(30):

		idade.append(int(input()))
		altura.append(float(input()))

	for c in range(30):

		if idade[c] > 13 and altura[c] < (sum(altura) / len(altura)):

			x += 1

	print("\n%d alunos com mais de 13 anos possuem altura inferior à média dos alunos." % x)