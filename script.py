fhand = open('err.jb')
for line in fhand:
	line = line.rstrip()
	if line.find('skipcodes') == -1:
		continue
	print line
