def is_isogram(string):
	seen = set()
	for x in string.lower():
		if x in seen:
			if x.isalpha():
				return False
		else:
			seen.add(x)

	return True
