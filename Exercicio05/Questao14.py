meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
	t = []

	print("Digite as temperaturas médias dos doze meses do ano (de Janeiro a Dezembro): ")

	for c in range(12):

		t.append(float(input()))

	mediaAnual = sum(t) / 12

	print()

	for c in range(12):

		if t[c] > mediaAnual:

			print("%s: %.2f." % (meses[c], t[c]))