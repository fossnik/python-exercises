def largest_product(series, size):
	if not series:
		raise Exception("ValueError")

	if size > len(series):
		raise Exception("ValueError")

	max = 0

	index = 0
	while index <= len(series) - size:
		temp = 1
		for x in range(0, size):
			temp *= int(series[index + x])
		index += 1
		if temp > max:
			max = temp

	return max