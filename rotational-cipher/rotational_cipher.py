import re
def rotate(text, key):
	remit = ""
	for c in text:
		if re.match('[a-z]', c):
			remit += chr(((ord(c) - ord('a')) + key) % 26 + ord('a'))
		elif re.match('[A-Z]', c):
			remit += chr(((ord(c) - ord('A')) + key) % 26 + ord('A'))
		else:
			remit += c
	return remit