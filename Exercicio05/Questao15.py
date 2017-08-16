notas = []
	x = 0
	y = 0

	print("Digite as notas (-1 encerra): ")
	 
	while True:
	 
	    n = float(input())
	 
	    if n == -1:
	 
	        break
	 
	    notas.append(n)
	 
	print("\n%d valores foram lidos." % len(notas))
	print("Valores lidos:", end = " ")
	 
	for c in range(len(notas) - 2):
	 
	    print("%.2f" % notas[c], end = ", ")
	 
	print("%.2f" % notas[len(notas) - 2], end = " e ")
	print("%.2f" % notas[len(notas) - 1], end = ".\n")
	 
	notasInvertidas = notas[:: -1]
	 
	print("Valores na ordem inversa à que foram lidos: ")
	 
	for c in range(len(notasInvertidas)):
	 
	    print("%.2f" % notasInvertidas[c])
	 
	print("Soma dos valores: %.2f." % sum(notas))
	print("Média dos valores: %.2f." % (sum(notas) / len(notas)))
	 
	for c in range(len(notas)):
	 
	    if notas[c] > (sum(notas) / len(notas)):
	 
	        x += 1
	 
	print("Quantidade de notas acima de sua média: %d." % x)
	 
	for c in range(len(notas)):
	 
	    if notas[c] < 7:
	 
	        y += 1
	 
	print("Quantidade de notas abaixo de 7: %d\n\nFim." % y)