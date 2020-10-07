# 由于打印对象和打印self得到的内存地址相同，所以self指的是调用该函数的对象
# 1.定义洗衣机类
class Washer():
    def wash(self):  #这个函数即实例方法或对象方法
        print("能洗衣服")
        print(self)

# 2.创建对象
haier = Washer()

# 3.验证结果
# 打印haier对象
print(haier)

# 使用wash功能--实例方法/对象方法--对象名.wash()
haier.wash()