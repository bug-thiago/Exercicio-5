n = []

print("Forneça as notas: ")

	for c in range(4):

		n.append(float(input()))

print("\nNotas:", end = " ")

	for c in range(4 - 1):

		print("%.2f" % (n[c]), end = ", ")

print(n[3])

	soma = 0

	for c in range(4):

soma += n[c]

print("Média: %.2f" % (soma / 4))