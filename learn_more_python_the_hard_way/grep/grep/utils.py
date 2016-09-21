import re
import os

def convert_patterns(patterns):
	results = []
	# for each pattern
	for pattern in patterns:
		# make a regex with it
		expr = re.compile(pattern)
		results.append(expr)

	# return the results
	return results

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

def apply_patterns(files, patterns):
	# for each file in files
	for fname in files:
		# open the file and read the lines
		lines = open(fname).read()
		for line in lines:
			# for reach pattern
			for pattern in patterns:
				# if pattern found in contents
				if pattern.search(line):
					# print file, line number, line
					print "%s: %s" % (os.path.join(fname), line)