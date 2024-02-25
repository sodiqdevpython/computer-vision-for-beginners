import numpy as np

def task1():
    x = np.array([2,3,4])
    print(x)

def task2():
    x = np.array([2,3,4.0, 200], dtype=np.int8)
    print(x)

def task3():
    x1dim = np.array(
        [1,2,3],
        dtype=np.int8
    )
    print(x1dim.ndim, "o'lchamli array") #! bu 1 dimension

    x2dim = np.array(
        [
            [1,2,3],
            [4,5,6]
        ],
        dtype=np.int8
    )
    print(x2dim.ndim, "o'lchamli array")

    x3dim = np.array([
        [
            [1,2,3],
            [2,5,7]
        ],
        [
            [1,3,3],
            [1,3,1]
        ]
    ],dtype=np.int8
    )
    print(x3dim.ndim, "o'lchamli array")
    print(x3dim)


def homework():
    x = np.array([
        [1],
        [2],
        [5]
    ], dtype=np.int8)
    print(x.shape)
    y = np.array([
        [1,2,3]
    ], dtype=np.int8)
    print(y.shape)
    
    z = np.array([
        [3,5],
        [98,5]
    ], dtype=np.int8)
    print(z.shape)

homework()