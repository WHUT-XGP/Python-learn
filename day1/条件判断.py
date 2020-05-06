# -*- coding: utf-8 -*-
# 条件判断从上向下匹配，当满足条件时执行对应的块内语句，后续的elif和else都不再执行。


height = 1.75
weight = 80.5
bmi = (weight / (height ** 2))
print('bmi=%.2f' % bmi)
if bmi < 18.5:
    print("过轻")
elif bmi < 25:
    print("正常")
elif bmi < 28:
    print("过重")
elif bmi < 32:
    print("肥胖")
else:
    print("严重肥胖")
