import numpy as np

def task1():
    arr1 = np.array([
        [9,5],
        [3,4],
        [3,0]
    ], dtype=np.int8)

    print(arr1[2][1]) #! bu eski yo'li sekinroq
    print(arr1[2, 1]) #! bu to'g'ri va tezroq bo'ladi

task1()