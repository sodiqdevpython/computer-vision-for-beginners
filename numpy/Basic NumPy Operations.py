import numpy as np

def task1():
    a = np.array([1,2,3])
    b = np.ones(3)
    print(a+b) #! a va b arraylarni qo'shish uchun

    print(a*b) #! a va b arraylarni ko'paytirish uchun

    print(a-b) #! a va b arraylarni ayirish uchun

    print(a/b) #! a va b arraylarni bo'lish uchun

task1()

def task2():
    x = np.array([1,2,3])
    y = np.array([2,5,3])
    
    print(x==y)

    print(x<y)

task2()