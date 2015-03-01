def gc_count():
	"""Basic GC Count function """
	a = 0
	t = 0
	g = 0
	c = 0

	type = raw_input("Please enter the data entry type (1=txt file, 2=direct entry): ")

	if type == "1":
		filename = raw_input("Please enter the path to the txt file: ")
		file = open(filename, "r")
		dna = file.read()
	else:
		dna = raw_input("Please enter the DNA string: ")	

	dna = list(dna)

	for i in range(len(dna)):
		if dna[i] == "A":
			a += 1
		elif dna[i] == "T":
			t += 1
		elif dna[i] == "G":
			g += 1
		elif dna[i] == "C":
			c += 1
		else:
			print "Invalid character, %s" % (dna[i])

	if type == "1":
		file.close()

	print "A: %s, T: %s, G: %s, C: %s" % (a, t, g, c)
	return a, t, g, c
		
gc_count()
