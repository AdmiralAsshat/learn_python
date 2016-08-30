## itertools.permutations(iterable [,r])

##      Return successive r length permutations of elements in the iterable.

##      If r is not specified or is None, then r defaults to the length of the
##      iterable and all possible full-length permutations are generated.

##      Permutations are emitted in lexicographic sort order. So, if the input
##      iterable is sorted, the permutation tuples will be produced in sorted
##      order.

##      Elements are treated as unique based on their position, not on their
##      value. So if the input elements are unique, there will be no repeat
##      values in each permutation.

    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210

import itertools

letters = 'AF'
perms = itertools.permutations('123', len(letters))

print perms
for perm in perms:
    print perm