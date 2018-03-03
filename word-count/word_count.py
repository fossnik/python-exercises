import re
def word_count(phrase):
	tally = {}
	# fix multiple whitespace instances
	fix = re.sub("\W\W+", " ", phrase)
	# replace anything that's not a letter or apostrophe (negative lookahead)
	fix = re.sub("(?!')\W+", " ", fix)
	# replace underscores
	fix = re.sub("_", " ", fix)

	for x in fix.lower().split():
		if not x in tally:
			tally[x] = 1
		else:
			tally[x] = tally[x] + 1

	return tally
