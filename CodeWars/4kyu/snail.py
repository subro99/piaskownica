"""To refactor"""

def snail(snail_map):
    x, y = 0, 0
    xwyk = 0
    ywyk = 0
    petla = 0
    xend = len(snail_map[0])-1
    yend = len(snail_map)-1
    size = len(snail_map[0])*len(snail_map)
    print(size)
    result = []
    while True:
        if len(result) >= size:
            break
        result.append(snail_map[y][x])
        if x < xend and y == ywyk:
            print("1")
            print(result)
            if x == xend-1:
                ywyk += 1
            x += 1
        elif x == xend and y < yend:
            print("2")
            print(result)
            y += 1
        elif x > xwyk:
            print("3")
            print(result)
            x -= 1
        elif y >= ywyk:
            print("4")
            print(result)
            print("tera to")
            print(result)
            print(f"y={y}, ywyk={ywyk},xwyk={xwyk}")
            y -= 1
            if y == ywyk:
                print("czy to sie wykonuje?")
                xwyk += 1
                x = xwyk-1
                y = ywyk
                xend -= 1
                yend -= 1
        else:
            break
    return result


array = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]
         ]
a = snail(array)
print(a)
