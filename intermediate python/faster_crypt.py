
# Functions we will create:

#    - solve   --> Runs thru all possible combinations testing each for valid
#    - fill_in --> Create a new formula replacing letters with numbers
#    - valid   --> Tests our filled-in string
#from __future__ import division

import cProfile
import re, string, itertools

def fast_solve(rawFormula):
    f, letters = compile_formula(rawFormula)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = string.maketrans(letters, ''.join(map(str, digits)))
                return rawFormula.translate(table)
        except ArithmeticError:
            pass

def compile_formula(rawFormula, debug=True):
    """
    Compile Formula into a function. (Uppercase letters are important)
    Returns the function as well as the letters used as arguments in the function
    """
    letters = ''.join(set(re.findall('[A-Z]', rawFormula)))
    params = ', '.join(letters)
    partitions = map(compile_partition, re.split('([A-Z]+)', rawFormula))
    formula = ''.join(partitions)
    f = 'lambda {}: {}'.format(params, formula)
    if debug: print f
    return eval(f), letters
    
    
def compile_partition(formulaPartition):
    """
    Compile a formula Partition of UPPER case letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase Partitions unchanged: compile_word('+') => '+'
    """
    if formulaPartition.isupper():
        terms = [('{}*{}'.format(10**i, d)) \
                 for (i, d) in enumerate(formulaPartition[::-1])]
        return '('+'+'.join(terms)+')'
    else:
        return formulaPartition

#################   OLD METHOD   #########################

def solve(rawFormula):
    """
    rawFormula = "SEND + MORE = MONEY"
    Test all possible translations between Character string and Numbered String
    Return the Solution to the puzzle or None is no solution is found.
    """
    for formula in fill_in(rawFormula):
        if valid(formula):
            return formula
    return None

def fill_in(rawFormula):
    """
    Generate all possible translations between Character string and Numbered String.
    """
    letters = ''.join(set(re.findall('[A-Z]', rawFormula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield rawFormula.translate(table)

    
def valid(formula):
    """
    Formula is valid only if it has no leading zero on any of it's numbers
    and the formula evaluates as True.
    Returns True or False
    1/0 = 1 --> ERROR, Dividing by Zero
    """
    try:
        return not re.search(r'\b0[0-9]', formula) and eval(formula) is True
    except ArithmeticError:
        return False

#cProfile.run("solve('SEND + MORE == MONEY')")
cProfile.run("fast_solve('SEND + MORE == MONEY')")
