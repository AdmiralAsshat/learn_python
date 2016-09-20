import re

def convert_patterns(patterns):
	results = []
	# for each pattern
	for pattern in patterns:
		# make a regex with it
		expr = re.compile(pattern)
		results.append(expr)
	# return the results
	return results