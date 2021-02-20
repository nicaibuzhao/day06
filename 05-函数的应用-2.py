# 练习1: 写一个函数求三个数的和
def sum(a, b, c):
    result = a + b + c
    return result


# 练习2: 写一个函数求三个数的平均值
def avg(a, b, c):
    result = sum(a, b, c)
    return result / 3

print(avg(1,1,1))