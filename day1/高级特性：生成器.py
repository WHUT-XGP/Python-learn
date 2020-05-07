# -*- coding: utf-8 -*-
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 创建一个generator：
# 第一种方法：把一个列表生成式的[]改成()
L = [x * x for x in range(10)]
print(L)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

L = (x * x for x in range(10))
print(L)  # <generator object <genexpr> at 0x000001E291D4AF90>  这既是一个generator

# 可以通过next()函数获得generator的下一个返回值
print(next(L))
print(next(L))
print(next(L))
print(next(L))
print(next(L))

# 通过循环获得：
for n in L:  # 会接后续
    print(n)

# 多赋值语句：
n, a, b = 0, 0, 1


# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(5)


# 将斐波拉契数列改为生成器generator
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print->yield
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def odd():
    print('step1')
    yield 1
    print('step2')
    yield 3
    print('step3')
    yield 5


# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中


# 迭代器

