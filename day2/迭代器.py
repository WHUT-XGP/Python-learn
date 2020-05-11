from collections.abc import Iterable
from collections.abc import Iterator

print(isinstance([], Iterable))  # True
print(isinstance((x * x for x in range(10)), Iterable))  # True

# list、dict、str虽然是Iterable，却不是Iterator。
print(isinstance('abc', Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))

# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter('abc'), Iterator))  # True
