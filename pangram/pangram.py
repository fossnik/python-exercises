def is_pangram(sentence):
	seen = set()
	for x in sentence.lower():
		if x.isalpha():
			seen.add(x)

	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for c in alphabet:
		if not c in seen:
			return False

	return True
