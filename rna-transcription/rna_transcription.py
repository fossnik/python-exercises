def to_rna(dna_strand):
	nucleotides = {
	'G' : 'C',
	'C' : 'G',
	'T' : 'A',
	'A' : 'U'
	}

	remit = "";
	for x in dna_strand:
		try:
			remit += nucleotides[x]
		except:
			raise ValueError("Only G, C, T, or A")

	return remit;
