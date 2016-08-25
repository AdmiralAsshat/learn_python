"""
Simulation of Web App Architecture

Service: The Russian Peasant's Algorithm

Architecture Include:

 - App Computer (Modules)
 - Database (--) --> Russian Peasant Algorithm
 - Load Balancer (Algorithm)

+-----+   +-----+   +-----+
| APP |   | APP |   | APP |
|  1  |   |  2  |   |  3  |
+-----+   +-----+   +-----+
"""


## How does a load balancer work?

## 1)   Random
## 2)   Looping
## 3)   Load Based

## Import Servers (modules)
import computer1
import computer2
import computer3

## Server names
SERVERS = [computer1, computer2, computer3]

import itertools
## Infinite Loop Iterator
cycle = itertools.cycle(SERVERS)

def get_server():
    """
    Your code in this function.
    No Inputs
    Output: Print the server name
    """
    global cycle
    return cycle.next()

## Testing the function
if __name__ == '__main__':
    from random import randint
    ## simulate a number of requests with this loop
    for i in range(10):
        ##: Generate some 'Requested' numbers
        # a = randint(5,99)
        # b = randint(5,99)
        z = randint(1,21)
        a = [12,86,179,34,70,23,55][z%7]
        b = [71,15,44,236,11,99,32][z%7]

        ## Run the load balancer algorithm to get us a computer
        server = get_server()

        ## Print the results
        print server.printName()
        print server.multiplyHandler(a,b)
        print server.lastMultipliedHandler()
        print " "