# -*- coding: utf-8 -*-

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])  # 95
d['AX'] = 20
print(d)  # {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'AX': 20}

d['AX'] = 666
print(d)  # {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'AX': 20}

# 判断key是否存在
# 一是通过in判断key是否存在：
print('Thomas' in d)  # False
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('AX', -2))  # 666
print(d.get('LCX', -2))  # -2
print(d.get('LCX'))  # None

# 使用pop(key)的方法来删除key-value对(注意pop会返回value值）
print(d.pop('Bob'))  # 75
print(d)  # {'Michael': 95, 'Tracy': 85, 'AX': 666}

# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。

# 而list相反：
# 查找和插入的时间随着元素的增加而增加
# 占用空间小，浪费内存很少。


# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合：
s = set(['dda', 'hgn', 'ax'])
print(s)  # {'hgn', 'dda', 'ax'}

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
s.add('ykh')  # {'dda', 'ax', 'hgn', 'ykh'}
s.add('ax')
print(s)
# 通过remove(key)方法可以删除元素：
s.remove('hgn')  # {'dda', 'ax', 'ykh'}
print(s)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
# |并集 &交集
print(s1 | s2)  # {1, 2, 3, 4}
print(s2 & s1)  # {2, 3}
# TODO:继续学习廖雪峰Python


