# python可以使用-1,-2等索引值来反向对数组进行索引
# python使用append方法来为数组添加元素
classmate = ['AX']
print(classmate)  # ['AX']
classmate.append('ykh')
print(classmate)  # ['AX', 'ykh']

# python的数组同样是引用机制
classmate_copy = classmate
print(classmate_copy)  # ['AX', 'ykh']
classmate.append('hgn')
print(classmate_copy)  # ['AX', 'ykh', 'hgn']
classmate_copy.append('cj')
print(classmate)  # ['AX', 'ykh', 'hgn', 'cj']

# tuple 元组 即不可变之数组，使用括号进行定义(),所以也就没有insert() append方法

# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
t = ()
print(t)
# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t2 = (1,)
print(t2)
# tuple的每个元素，指向永远不变。但是指向的内容本身可变，也就是如果指向某个数组，那么改动该数组会导致变化
