# from itertools import permutations as perm


# def permutations(string):
#     result = []

#     all_perm = perm(string, len(string))
#     print(all_perm)
#     result = ["".join(x) for x in perm(string, len(string))]
#     return result
result=[]
def permutations(string):
    if len(string)==1:
        return string
    for i,char in enumerate(string):
        leftover=string[:i]+string[i+1:]
        return char+permutations(leftover)


print(permutations("abc"))

