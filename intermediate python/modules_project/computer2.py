import fake_database

CACHE = {}

def printName():
    return str(__name__)

def updateLastMultiplied(a,b,result):
    key = 'lastFive'
    lastFiveList = CACHE.get(key)
    if lastFiveList:
        if len(lastFiveList) >= 5:
            ## The list already had five items in it
            newList = lastFiveList[1:]
            newList.append('{}x{}={}'.format(a,b,result))
            CACHE[key] = newList
        else:
            ## The list had less than five items
            lastFiveList.append('{}x{}={}'.format(a,b,result))
            CACHE[key] = lastFiveList
    else:
        ## There was not a cache so create one
        CACHE[key] = ['{}x{}={}'.format(a,b,result)]
            

def lastMultipliedHandler():
    """
    Write this function.
    Inputs : None
    Outputs: The last multiplied result
    This is the last 5 multiplied questions/answers
    """
    key = 'lastFive'
    if key in CACHE:
        return "Last 5 = {}".format(CACHE[key])
    else:
        return "Russian not used before."


def multiplyHandler(a, b):
    """
    Write this function.
    Inputs : a, b representing Numbers as arguments from the request.
    Outputs: The result of those two numbers being sent thru
                The Russuan Peasant's Algorithm.
    """
    cacheKey = (a,b)
    if cacheKey in CACHE:
        return CACHE[cacheKey]
    else:
        result = fake_database.rpa(a,b)
        updateLastMultiplied(a,b, result)
        CACHE[cacheKey] = result
        return 'Latest Result: {}'.format(result)
        lastMultipliedHandler()

if __name__ == '__main__':
    multiplyHandler(2, 3)
    multiplyHandler(7, 16)
    multiplyHandler(10, 20)
    multiplyHandler(33, 66)
    multiplyHandler(9, 150)
    multiplyHandler(5627, 9534)
    multiplyHandler(9999, 9999)