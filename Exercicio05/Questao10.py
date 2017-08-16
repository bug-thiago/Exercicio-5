A = []
	s = 0

	for c in range(10):

		A.append(int(input()))

	for c in range(10):

		s += pow(A[c], 2)

	print("\n%d" % s)