import math

"""
Solution don't match time requirements,
need to be improved in term of time complexity
"""

def sol_equa(n):
    result = []
    y = 0
    x = 0
    while x+2*y < n:
        x = math.sqrt(n+4*y**2)
        if x.is_integer():
            result.append([int(x), y])
        y += 1
    result.sort(reverse=True)
    return result