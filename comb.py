#!env python3

import sys
import itertools

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Provide the digits you want all the combinations for")
        sys.exit(1)

    chars = list(sys.argv[1])
    combs = list(itertools.permutations(chars))
    for comb in combs:
        print("".join(comb))
