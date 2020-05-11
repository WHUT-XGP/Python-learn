# -*- coding = utf-8 -*-
# @Time : 2020/5/11 15:37
# @Author : AX
# @File : 类与对象.py
# @Software: PyCharm
#
import time
def log(res):
    return time.time()
class Student(object):
    # __init__类似于构造函数
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.__private = 'kkk'

    def get_grade(self):
        if self.score >= 90:
            return 'a'
        else:
            return 'false'


bart = Student('ax', 100)


print(bart.get_grade())
print(bart.name)

