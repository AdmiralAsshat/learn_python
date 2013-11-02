i = 0
counter = raw_input("Number of times to iterate? ")
counter = int(counter)
print 'Number chosen: %d ' % counter

numbers = []

while i < counter:
	print "At the top i is %d" % i
	numbers.append(i)

	i += 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
	print num
