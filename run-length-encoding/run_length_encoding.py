def decode(string):
	remit = ""
	x = 0
	while x < len(string):
		if not string[x].isdigit():
			remit += string[x]
		else:
			prefix = ""
			while string[x].isdigit():
				prefix += string[x]
				x += 1
			for y in range(0, int(prefix)):
				remit += string[x]
		x += 1
	return remit

def encode(string):
	remit = ""
	x = 1
	while x <= len(string):
		count = 1
		try:
			while string[x] == string[x-1]:
				count += 1
				x += 1
		except IndexError:
			print("")

		if count > 1:
			remit += str(count) + string[x-1]
		else:
			remit += string[x-1]

		x += 1
	return remit