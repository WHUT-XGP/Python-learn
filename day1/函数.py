# -*- coding: utf-8 -*-

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs
print(a(-1))
# hex()十六进制整数

# pass可以用来作为占位符
# 使用isinstance()来进行参数检查

# Python函数可以返回多个值
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


# 返回的是元组
print(move(0, 0, 100, math.pi / 6))  # (86.60254037844388, 49.99999999999999)

x, y = move(0, 0, 100, math.pi / 6)
print(x, y)  # 86.60254037844388 49.99999999999999


# Python中默认函数参数可以使用=符号
# ps:默认参数必须指向不变对象！ 比如None
def enroll(name, gender, age=6, city="wuhan"):
    print("name=", name)
    print("age=", age)
    print("gender=", gender)
    print("city=", city)
    return


# enroll("ax", "man")
# enroll("ax", "man", city="益阳")

# 可变参数：可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
# 可以使用*用于将参数封装为tuple 即自动添加一个()
def calc(*numbers):
    sum_t = 0
    for n in numbers:
        sum_t = sum_t + n * n
    return sum_t


print(calc(1, 2, 3, 4))  # 30


def product(*L):
    ans = 1
    if L is None:
        return TypeError
    for l in L:
        ans *= l
    return ans


product(1, 2, 3, 4)


# 关键字参数:封装为dict，使用**符号进行定义
# 可以通过kw拿到对应数据
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
# 这种方式定义的函数如下：
def person1(name, age, *, city, job):
    print(name, age, city, job)


# 通过key=value的形式进行传参（自动转换为dict）
# ps：这种方式的包装是对外界数据的拷贝，所以不会影响到外界传入的实际数值
person('Bob', 35, city='Beijing')  # name: Bob age: 35 other: {'city': 'Beijing'}



# 递归：

