import matplotlib.pyplot as plt
import time
from timeit import timeit

code1 = """
nowa_lista = [x for x in lista]
"""
code2 = """
nowa_lista = []
for x in lista:
    nowa_lista.append(x)
"""
code3 = """
nowa_lista = list(map(lambda x: x, lista))
"""


def list_comp(lista):
    start_time = time.time()
    nowa_lista = [x**x for x in lista]
    return time.time() - start_time


def for_append(lista):
    start_time = time.time()
    nowa_lista = []
    for x in lista:
        nowa_lista.append(x**x)
    return time.time() - start_time


def list_map(lista):
    start_time = time.time()
    nowa_lista = list(map(lambda x: x**x, lista))
    return time.time() - start_time


def profile():
    time_list_comp = []
    time_for_append = []
    time_list_map = []


    Nls = [x for x in range(0, 10000, 100)]
    for N in Nls:
        n = [x for x in range(N)]
        setup = "lista="+str(n)
        time_list_comp.append(timeit(code1, number=100, setup=setup))
        time_for_append.append(timeit(code2, number=100, setup=setup))
        time_list_map.append(timeit(code3, number=100, setup=setup))

    colors = "r", "b", "g"
    fig, ax1 = plt.subplots(tight_layout=True)
    
    ax1.set_title("Creating new list Time complexity")
    ax1.set_xlabel("list size")
    ax1.set_ylabel("time",)
    ax1.plot(Nls, time_list_map, marker="o",color=colors[2], label='map')
    ax1.plot(Nls, time_for_append, marker="o",color=colors[1], label='for+append')
    ax1.plot(Nls, time_list_comp, marker="o",color=colors[0], label='list comp')
    
    plt.legend(loc='upper left')
    plt.savefig("list_comparison.png")
    plt.savefig("list_comparison.jpg")
    plt.show()


profile()
