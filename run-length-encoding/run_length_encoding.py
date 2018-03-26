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
	pass
