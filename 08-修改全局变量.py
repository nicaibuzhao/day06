# 练习: 已知全局变量 g_num = 0， 在函数内完成对全局变量的修改。

g_num = 0

def change():
    g_num = 10
    print(g_num)

change()
print(g_num)