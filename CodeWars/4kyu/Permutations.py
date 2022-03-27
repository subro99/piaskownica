from itertools import permutations as perm

def permutations(string):
    result = []
    all_perm = perm(string, len(string))
    print(all_perm)
    result = ["".join(x) for x in perm(string, len(string))]
    return set(result)