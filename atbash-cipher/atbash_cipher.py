import re

cipher = {
	'a': 'z',
	'b': 'y',
	'c': 'x',
	'd': 'w',
	'e': 'v',
	'f': 'u',
	'g': 't',
	'h': 's',
	'i': 'r',
	'j': 'q',
	'k': 'p',
	'l': 'o',
	'm': 'n',
	'n': 'm',
	'o': 'l',
	'p': 'k',
	'q': 'j',
	'r': 'i',
	's': 'h',
	't': 'g',
	'u': 'f',
	'v': 'e',
	'w': 'd',
	'x': 'c',
	'y': 'b',
	'z': 'a',
}

def encode(plain_text):
	output = ""
	count = 0
	regexp = re.compile(r'[a-zA-Z0-9]')
	for c in plain_text:
		if regexp.search(c):
			if count % 5 == 0 and count != 0:
				output += " "
			count += 1
			if c.isalpha():
				output += cipher[c.lower()]
			elif c.isdigit():
				output += c

	return output

def decode(ciphered_text):
	pass
