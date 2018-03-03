def distance(strand_a, strand_b):
	if not len(strand_a) == len(strand_b):
		raise ValueError("strands must be of equal length")

	hammingDistance = 0
	index = 0
	while (index < len(strand_a)):
		if not strand_a[index] == strand_b[index]:
			hammingDistance += 1
		index += 1

	return hammingDistance
