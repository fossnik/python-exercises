def sieve(limit):
	if limit < 2:
		return []

	notPrime = []
	for i in range(2, limit):
		number = i
		while number <= limit + i:
			number += i
			notPrime.append(number)

	remit = [2]
	for i in range(3, limit + 1):
		if i not in notPrime:
			remit.append(i)

	return remit
