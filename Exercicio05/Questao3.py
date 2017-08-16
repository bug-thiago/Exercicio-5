n = []

	for c in range(10):

		try:

			n.append(float(input()))

		except:

			print("Não foram digitados valores reais.")

			break
			
	print()

	for c in range(10 - 1, -1, -1):

		print(n[c])