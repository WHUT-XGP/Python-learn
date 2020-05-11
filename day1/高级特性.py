# -*- coding: utf-8 -*-
# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[0:3])  # ['Michael', 'Sarah', 'Tracy']
# ps:索引不包括3 为[0,3)

print(L[:3])  # ['Michael', 'Sarah', 'Tracy'] 如果其下标为0或者len长度，则可以省去
print(L[1:])  # ['Sarah', 'Tracy', 'Bob', 'Jack']
print(L[:])  # ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 支持负数切片
print(L[:-2])  # ['Michael', 'Sarah', 'Tracy']

# 更多用法：
L = list(range(0, 100))
# 使用切片进行翻转字符串
s = 'ddsss'
sr = s[::-1]
print(sr)
# 支持分割长度进行切片,如下添加一个:20则可以分割切片
print(L[0:100:20])  # [0, 20, 40, 60, 80]

# tuple也可以进行切片

# PS：Python没有提供对str的截取函数，因为一般通过切片完成
s = "123456789"
print(s[2:4])  # 34

# 迭代
# 1.dict的迭代方法 .values()迭代值 .keys()迭代键 .items()同时迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)  # a b c
for key in d.keys():
    print(key)  # a b c
for value in d.values():
    print(value)  # 1 2 3
# for循环其实可以同时使用两个甚至多个变量
for key, value in d.items():
    print(key, value)

# 如何判断一个对象是否是可迭代对象？
# 1.通过collections.abc模块的Iterable类型和isinstance函数来进行判断：
from collections.abc import Iterable

print(isinstance('abcd', Iterable))  # True
print(isinstance([1, 2, 3, 4], Iterable))  # True

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for key, value in [(1, 2), (3, 4), (5, 6)]:
    print(key, value)
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)
    # 0 a
    # 1 b
    # 3 c


# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if len(L) < 1:
        return (None, None)
    max = L[0]
    min = L[0]
    for value in L:
        if value > max:
            max = value
        if value < min:
            min = value
    return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

# 列表生成器：
L = [x * x for x in range(1, 5)]
print(L)  # [1, 4, 9, 16]

# 相当于：
L = []
for x in range(1, 5):
    L.append(x * x)

# 其后还可以跟随if条件判断,进行筛选（注意如果判断是放在后面不能加else）
L = [x * x for x in range(1, 5) if x % 2 == 0]
print(L)  # [4, 16]
# 如果判断放在前面，则必须添加else,类似于对x进行判断处理（也就是对表达式进行改变）
L = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(L)  # [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
# 上述类似于：
L = []
for x in range(1, 11):
    if x % 2 == 0:
        L.append(x)
    else:
        L.append(-x)
print(L)

# 还可以跟多重循环，进行全排列
L = [m + n for m in 'ABC' for n in 'opq']
print(L)  # ['Ao', 'Ap', 'Aq', 'Bo', 'Bp', 'Bq', 'Co', 'Cp', 'Cq']
