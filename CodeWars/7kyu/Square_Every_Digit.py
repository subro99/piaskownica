def square_digits(num):
    string=str(num)
    l=[int(digit) for digit in string]
    squared=[]
    for i in l:
        squared.append(str(i**2))
        
    return int("".join(squared))