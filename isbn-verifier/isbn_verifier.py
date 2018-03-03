import re
def verify(isbn):
	isbn = re.sub("[^0-9X]", "", isbn)

	if not len(isbn) == 10:
		return False

	summ = 0
	if isbn[9] == "X":
		summ += 10

	index = 10
	for x in re.sub("[^0-9]", "", isbn):
		summ += int(x) * index
		index -= 1

	return summ % 11 == 0
