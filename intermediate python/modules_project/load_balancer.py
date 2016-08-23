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

## Server names
SERVERS = ['APP1', 'APP2', 'APP3']

def get_server():
    """
    Your code in this function.
    No Inputs
    Output: Print the server name
    """
    pass

## Testing the function
if __name__ == '__main__':
    for i in range(8):
        get_server()

## APP1
## APP2
## APP3
## APP1
## APP2
## APP3
## APP1
## APP2
## APP3
        