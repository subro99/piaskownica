def array_diff(a, b):
    for el_b in b:
        while el_b in a:
            a.remove(el_b)
    return a