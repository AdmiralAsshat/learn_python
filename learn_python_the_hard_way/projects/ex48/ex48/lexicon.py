## Lexicon Module
## Purpose: Parses user input for keywords
## Likely categories of keywords:
## - Nouns
## - Verbs
## - Numbers
## - Directions
## - Prepositions?

def scan(input):
	## Split input on space delimiter into words
	## Parse words for keywords
	words = input.split()
	sentence = []

	## Categories of words
	DIRECTIONS = ['north', 'south', 'east', 'west']
	NOUNS = ['bear', 'princess', 'IAS', 'chicken', 'Satan']
	VERBS = ['go', 'eat', 'kill', 'punch', 'defenestrate']
	PREPOSITIONS = ['at', 'in', 'of', 'from']

	## Loop through words
	for word in words:
		## Figure out type of each word
		if word in DIRECTIONS:
			sentence.append(('direction', word))
		elif word in NOUNS:
			sentence.append(('noun', word))
		elif word in VERBS:
			sentence.append(('verb', word))
		elif word in PREPOSITIONS:
			sentence.append(('preposition', word))
		elif word.isdigit():
			sentence.append(('number', int(word)))
		else:
			sentence.append(('error', word))
			
	## Return a "sentence" (list of tuples) of word type and word
	return sentence