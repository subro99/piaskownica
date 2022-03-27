# wrzucic jako parametr do partitions

# def partitions(n, result):
#     if isinstance(n, int):
#         result.append([n])
#         new1 = [n]
#     else:
#         new1 = n.copy()
#         if len(n) == sum(n):
#             return len(result)
#         new3 = n.copy()
#         new3[0] -= 1
#         new3[1] += 1
#         if new3[1] <= new3[0]:
#             result.append(new3)
#     new1[0] -= 1
#     new1.append(1)
#     if new1[1] <= new1[0]:
#         result.append(new1)
#         # result+=new1
#         return partitions(new1, result)

from pprint import pprint


def partitions(n, result=[]):
    if isinstance(n, int):
        result.append([n])
        # new1 = [n-1,1]

    # while True:
    #     if len(new1)>1:
    #         new1[0]-=1
    #         new1[1]+=1
    #         if new1[1]<=new1[0]:
    #             result.append(new1.copy())
    #         else:break
    new1 = [n]

    while True:
        new2 = new1.copy()
        while len(new1) > 1:
            if len(new2) > 1:
                new2[0] -= 1
                new2[1] += 1
                if new2[1] <= new2[0]:
                    result.append(new2.copy())
                else:
                    break
        new1[0] -= 1
        new1.append(1)
        if new1[1] <= new1[0]:
            result.append(new1.copy())
        else:
            break

    return result
    # if len(n) == sum(n):
    #     return len(result)
    # new3 = n.copy()
    # new3[0] -= 1
    # new3[1] += 1
    # if new3[1] <= new3[0]:
    #     result.append(new3)

    # new1[0] -= 1
    # new1.append(1)
    # if new1[1] <= new1[0]:
    #     result.append(new1)
    #     # result+=new1
    #     return partitions(new1, result)

# def partitions(n,result=None):
#     if result is None:
#         result=[]
#     if isinstance(n, int):
#         result.append([n])
#         new1=[n]
#     else:
#         new1=n.copy()
#         if len(n)==sum(n):
#             return result

#     new1[0]-=1
#     new1.append(1)
#     if new1[1]<=new1[0]:
#         result.append(new1)
#         # result+=new1
#         # new2=new1.copy()
#     return partitions(new1,result)
#     # result=[n]
#     # while n>1:
#     #     n-=1
#     #     result.append([n,1])


l = []
pprint(partitions(10, l))

# lista = []
# liczba = 5
# lista.append(liczba)
# print(lista)
# liczba = 4
# print(lista)
# liczba=5
# t=[liczba,4]
# print(isinstance(liczba, int))
# print(t)
# new=[t]
# print(new)
# print(type(t))
