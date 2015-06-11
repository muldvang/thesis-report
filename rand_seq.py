import random
import sys

def random_sequence(n, alphabet_size):
    for _ in range(n):
        sys.stdout.write(str(random.randrange(0, alphabet_size)) + " ")

if not len(sys.argv) == 3:
    print('Usage: rand_seq length alphabet-size')
    exit(1)

N = int(sys.argv[1])
alphabet_size = int(sys.argv[2])
random_sequence(N, alphabet_size)
