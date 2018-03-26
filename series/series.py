def slices(series, length):
	if length > len(series):
		raise ValueError("slice too long")
	if length < 1:
		raise ValueError("slice too short")
	remit = []
	index = 0
	while index <= len(series) - length:
		subarray = []
		for x in range(0, length):
			subarray.append(int(series[index + x]))
		remit.append(subarray)
		index += 1
	return remit