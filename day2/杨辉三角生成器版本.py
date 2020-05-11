# 练习：生成器杨辉三角
def triangles():
    prev, temp = None, None
    while True:
        if prev == None:
            count = 0
        else:
            count = len(prev)
        temp = []
        # 当前的长度是上层的长度加1，则循环count+1次
        for i in range(count + 1):
            # 第一个和最后一个都是1
            if (i == 0 or i == count ):
                temp.append(1)
                continue
            temp.append(prev[i] + prev[i - 1])
        yield temp
        prev = temp
        print(temp)


n = triangles()
next(n)
next(n)
next(n)
next(n)
next(n)
next(n)