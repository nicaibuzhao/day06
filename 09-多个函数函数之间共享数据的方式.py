# 练习: 能够写出多个函数之间共享数据的两种方式

# ===============全局变量============




# ===============return返回值========
def return_data():
    data = "ok"
    return data

def show_data():
    data = return_data()
    print(data)
















