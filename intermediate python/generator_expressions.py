## Generator functions

## Generators are a simple and powerful tool for creating iterators.
## They are written like regular functions but use the yield statement
## whenever they want to return data

def count(start, end = None):
	i = start
	while i <= end or end == None:
		yield i
		i += 1

c = count(0)
print c

for i in range(100):
	print c.next()