# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，
# 在保存源代码时，就需要务必指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 短除 //
print(4 / 3)  # 1.3333333333333333
print(4 // 3)  # 1

# ord()函数： 获取字符的整数表示 chr()函数把编码转换为对应的字符
print(ord('A'))  # 65
print(chr(65))  # A

# 直接通过编码打印字符
print('\u4e2d\u6587')  # 中文

# 使用r标识符
print(r'\u4e2d\u6587')  # \u4e2d\u6587

# 使用多层表示法
print('''你好！
我是AX！
你也可以叫我广平''')  # 你好！
# 我是AX！
# 你也可以叫我广平

# python中的字符类型叫 str

# 也可以使用b标识符来进行编码,要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
print(b'ABC')

# encode方法（可以使用encode方法更改字符编码）
# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
# 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。在bytes中，无法显示为ASCII字符的字节，用\x##显示。
print('我是AX'.encode('gbk'))  # b'\xce\xd2\xca\xc7AX'

# decode方法（可以使用decode方法通过制定编码格式进行读取）

# 如果bytes中包含无法解码的字节，decode()方法会报错：
# print(b'\xce\xd2\xca\xc7AX'.decode('utf-8'))
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xce in position 0: invalid continuation byte

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
print(b'ABCD'.decode('utf-8'))  # ABCD
print(b'\xce\xd2\xca\xc7AX'.decode('gbk'))  # 我是AX
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))  # 中

# len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
print(len(b'abc'))  # 3
print(len('abc'))  # 3
print(len('中文'))  # 2
print(len('中文'.encode('utf-8')))  # 6

# 占位符 %d 整数 %f 浮点数 %s 字符串 %x 十六进制整数
# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
# 如果需要打印为正常字符则可以使用%%进行转义

print("提高了%.1f%%" % ((85 - 72) / 72 * 100))

# 当str和bytes互相转换时，需要指定编码。最常用的编码是UTF-8。Python当然也支持其他编码方式，
# 但这种方式纯属自找麻烦，如果没有特殊业务要求，请牢记仅使用UTF-8编码。
