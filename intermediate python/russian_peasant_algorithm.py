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

def rpa(x, y):
  total = 0
  while(x > 0):
#  	print("debug: " + str(x) + "," + str(y))
  	if (x % 2 == 1):
  	  total +=y
  	x /=2
  	y *=2
  print total

def main():
	rpa(25, 48)		#1200
	rpa(135, 233)	#31455
	rpa(666, 999)	#665334
	rpa(255, 1000)	#255000

if __name__ == '__main__':
	main()