##: The Russian Peasant's Algorithm
##: Been around a ling time (Seventeenth Century B.C.)

##: Multiply two numbers together.
##: Requirements: multiply by 2, divide by 2, and add numbers

##: AKA = Mediation and Duplation Method

##:
##: Inputs -> two numbers
##: Output -> the solution to those two numbers
##:				multiplied together using the Russian Peasant Algorithm

## Example:
##24 	*	 36		#EVEN: Disregard
##12 	*	 72		#EVEN: Disregard
##6 	*	144 	#EVEN: Disregard
##3 	* 	288		#ODD: Add
##1 	*	576 	#ODD: Add
##--------------
## 288 + 576 = 864

import time

def rpa(x, y):
  total = 0
  while(x > 0):
  	if (x % 2 == 1):	#If left-side is odd,
  	  total +=y			#keep right-side number
  	x = x >> 1			#Bit-shift to divide by two
  	y = y << 1			#Bit-shift to multiply by two
  return total

def test_rpa():
	assert rpa(25, 48) == 1200
	assert rpa(135, 233) == 31455
	assert rpa(666, 999) == 665334
	assert rpa(255, 1000) == 255000
	print "All tests of function rpa successful."

	start_time = time.time()
	print rpa(25, 48)		#1200
	print "Russian Algorithm took %f seconds" % (time.time() - start_time)

def main():
	test_rpa()

if __name__ == '__main__':
	main()