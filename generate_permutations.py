import sys
import random

#The original function
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

def generate_random_permutations(in_word):
    """Function that generates given word random permutations"""
    #Duplicate values will be ignored
    permutations_set =set()
    count = 20 if len(word)>20 else len(word)
    while len(permutations_set)< count:
        random.shuffle(in_word)
        permutation = ''.join(in_word)
        permutations_set.add(permutation)
    for p in permutations_set:
        print(p)

if len(sys.argv) != 2:
    sys.stderr.write('Exactly one argument is required\n')
    sys.exit(1)

word = sys.argv[1]

#generate_permutations(list(word), len(word)-1)
generate_random_permutations(list(word))
