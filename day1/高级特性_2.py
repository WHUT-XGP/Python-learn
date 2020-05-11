# -*- coding: utf-8 -*-
# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os

L = [dir for dir in os.listdir('.')]
print(L)  # ['dict&set.py', 'list&tuple.py', 'Python字符.py', '函数.py', '循环.py', '条件判断.py', '高级特性.py', '高级特性_2.py']
L = [dir for dir in os.listdir('../')]
print(L)  # ['.git', '.idea', 'day1', 'README.md']
# 使用绝对路径：
L = [dir for dir in os.listdir('F://Python Demo/Python-learn')]
print(L)
# 改变值：
L = [dir.lower() for dir in os.listdir('F://Python Demo/Python-learn')]
print(L)  # ['.git', '.idea', 'day1', 'readme.md']
