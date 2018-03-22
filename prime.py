def odd():
    n=1
    yield 2
    while True:
        n=n+2
        yield n
#首先可以明确一点就是： 素数或质数 绝对是2和大于等于2的奇数组成

def filterf(n):
    return lambda x:x%n>0
#埃氏筛法（在生成器中，从最小开始去掉他们的倍数：2，3，5...）
#lambda是一个匿名函数，结合下文它的用处理解


def primed():
    #yield 2
    temp=odd()#获取生成器
    while True:
        n=next(temp)#取第一个值
        yield n#生成生成器
        temp=filter(filterf(n),temp)#埃氏筛法，filter()函数

for n in primed():
    if n<1000:
        print(n)
    else:
        break

