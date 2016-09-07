class lexicon(object):
## Purpose: Parses user input for keywords
## Likely categories of keywords:
## - Nouns
## - Verbs
## - Numbers
## - Directions
## - Prepositions?

	def __init__(self):
	## Does it need to do anything special on init?
	pass

	def scan(self, input):
	## Split input on space delimiter into words
	## Parse words for keywords
	words = input.split()
	sentence = []
	##Categories of words
	DIRECTIONS = ['north', 'south', 'east', 'west']
	NOUNS = ['bear', 'princess', 'IAS', 'chicken', 'Satan']
	VERBS = ['go', 'eat', 'kill', 'punch', 'defenestrate']
	NUMBERS = ['1','2','3','4','5','6','7','8','9','0']
	PREPOSITIONS = ['at', 'in', 'of', 'from']
	## Loop through words
	for word in words:
		## Figure out type of each word
		if word in DIRECTIONS:
			sentence.append(('direction', word))
		else if word in NOUNS:
			sentence.append(('noun', word))
		else if word in VERBS:
			sentence.append(('verb', word))
		else if word in NUMBERS:
			sentence.append(('number', word))
		else if word in PREPOSITIONS:
			sentence.append(('preposition', word))
		else:
			sentence.append(('error', word))
	## Return a "sentence" (list of tuples) of word type and word
	return sentence