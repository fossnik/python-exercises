def hey(phrase):
	phrase = phrase.strip()

	if isallcaps(phrase):
		if phrase.endswith("?"):
			return "Calm down, I know what I'm doing!"
		else:
			return "Whoa, chill out!"

	if phrase.endswith("?"):
		return "Sure."

	if not phrase:
		return "Fine. Be that way!"

	return "Whatever."


def isallcaps(phrase):
	for x in phrase:
		if x.islower():
			return False

	return True
