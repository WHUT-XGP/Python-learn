# 此部分同js有众多相似之处
# 函数同样是变量名类似

# 高阶函数
def f(x, y, f):
    return f(x) + f(y)


print(f(-10, 100, abs))


# map/reduce
# Python内部内建了map()和reduce()
# map()函数接受两个参数，一个是函数，另一个是Iterable
# map将传入的函数依次作用到Iterable的每个元素上并将处理后的Iterable返回
def f(x):
    return x ** 2


r = map(f, [1, 2, 3, 4, 5])
print(r)  # <map object at 0x000002DEAEC99760>
print(list(r))  # [1, 4, 9, 16, 25]


# reduce类似于js
def add(x, y):
    return x + y


# 在Python 3里，reduce()函数已经被从全局命名空间里移除了，
# 它现在被放置在fucntools模块里。
# 要使用reduce()的话，要先引入from functools import reduce
from functools import reduce

reduce(add, [1, 2, 3, 4, 5])

# filter()过滤序列

# sorted()函数对List进行排序
# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，即之前常用的cmp，例如按绝对值大小排序
print(sorted([36, 5, -12, 9, -21], key=abs))

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


# Python同样有闭包的概念：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# lambda函数
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# lambda x: x*x 相当于
def f(x):
    return x * x
