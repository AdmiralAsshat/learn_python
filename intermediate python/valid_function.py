
# Functions we will create:

#    - solve   --> Runs thru all possible combinations testing each for valid
#    - fill_in --> Create a new formula replacing letters with numbers
#    - valid   --> Tests our filled-in string

import re

def solve(rawFormula):
    """
    Test all possible translations between Character string and Numbered string
    Return the Solution to the puzzle or None if no solution is found.
    """
    pass

def valid(formula):
    """
    Formula is valid only if it has no leading zero on any of its numbers
    and the formula evaluates as True.
    Returns True or False
    """
    try:
        # Is there a zero at beginning of formula?
        return not re.search(r'\b0[0-9]', formula) \
        and (eval(formula)) #Is the formula true?
    except ArithmeticError:
        return False
    except:
        return False

def test_valid():
    f='2+2==4'
    print("Formula: %s - %s" % (f, valid(f)))
    f='320+640==100'
    print("Formula: %s - %s" % (f, valid(f)))
    f='2-2==0'
    print("Formula: %s - %s" % (f, valid(f)))
    f='16*16==256'
    print("Formula: %s - %s" % (f, valid(f)))
    f='034+168==202'
    print("Formula: %s - %s" % (f, valid(f)))

if __name__ == '__main__':
    test_valid()