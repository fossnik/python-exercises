def flatten(iterable):
	remit = []

	for i in iterable:
		if i == 0:
			remit.append(i)
		elif i:
			if type(i) == type([]):
				remit = remit + flatten(i)
			else:
				remit.append(i)

	return remit
