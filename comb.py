#!/usr/bin/env python3

import sys
import itertools

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Provide the digits you want all the combinations for")
        sys.exit(1)

    chars = list(sys.argv[1])
    combs = list(set(itertools.permutations(chars)))
    combs.sort()

    n = 1
    for comb in combs:
        print(str(n)+": "+ "".join(comb))
        n+=1
