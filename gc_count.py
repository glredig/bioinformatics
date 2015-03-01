def gc_count():
	"""Basic GC Count function """
	filename = raw_input("Please enter the path to the txt file: ")
	file = open(filename, "r")
	a = 0
	t = 0
	g = 0
	c = 0

	dna = file.read()
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

	file.close()

	print "A: %s, T: %s, G: %s, C: %s" % (a, t, g, c)
	return a, t, g, c
		
gc_count()
