
#Try
#Except

userDefined = 'b'

class MyException(Exception):
	pass

try:
	#a = int(userDefined)
	raise MyException('My Exception Error!')
except ValueError:
	a = int(1)
	print 'Error', str(a)
except MyException as e:
	a = int(0)
	# print ("Error {}: {}").format(a,e)
	print("Error %d: %s" % (a, e))
except:
	print 'Error -1'
else:
	print a