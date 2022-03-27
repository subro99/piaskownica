def move_zeros(array):
    for element in array:
        if element==0:
            array.remove(0)
            array.append(0)
    return array