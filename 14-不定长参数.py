# 练习: 定义一个函数，可以接收不确定个数的位置参数和不确定个数的关键字参数

def fun(*args, **kwargs):
    result = 0
    # 遍历args获取每个位置参数
    for n in args:
        result += n

    for value in kwargs.values():
        result += value
    return result


print(fun(1, 2, a=1, b=2))