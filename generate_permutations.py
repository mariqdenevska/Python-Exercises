import sys, re
import math
import random

def generate_permutations(a, n):
    """Function that generates given word permutations"""
    if n == 0:
        print(''.join(a))
    else:
        for letter in range(n):

            generate_permutations(a, n-1)
            j=0 if len % 2 == 0 else letter
            a[j], a[n] = a[n], a[j]
        generate_permutations(a, len-1)

if len(sys.argv) != 2:
    sys.stderr.write('Exactly one argument is required\n')
    sys.exit(1)

word = sys.argv[1]

generate_permutations(list(word), len(word)-1)
