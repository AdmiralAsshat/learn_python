##: testing

##: WHY?
##: To Understand our Code better
##: To learn when we make a mistake
##: To know when we are finished
##: To ensure any future program changes/additions don't break out programs

def adding(a,b):
	return a + b

def test_adding():
	assert adding(3,4) == 7
	assert adding(3,2) == 5
	assert adding(99,49) == 148
	assert adding(1.5,2) == 3.5
	assert adding(1.5,1.5) == 3

	return "All Tests Pass for function adding()"

print test_adding()