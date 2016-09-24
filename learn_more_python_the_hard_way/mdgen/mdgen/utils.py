import os

def troll_directories(start):
	results = []

	# troll for all the directories like in find
	# traverse the directories for all files
	for root, dirs, files in os.walk(start):
		# for each file, see if pattern in filename
		for fname in files:
			# put the full path into the results
			results.append(os.path.join(root, fname))

	return results
