# 需要通过装饰器@staticmethod来进行修饰，静态方法既不用传递类对象，也不用传递实例对象(形参没有self/cls)
# 当方法中即不需要使用实例对象，也不需要使用类对象时，定义静态方法
# 取消不需要的参数传递，有利于减少不必要的内存占用和性能消耗
# 1.定义类，定义静态方法
class Dod():
    @staticmethod
    def info_print():
        print('这是一个静态方法')


# 2.创建对象
wangcai = Dod()

# 3.调用静态方法：类和对象
wangcai.info_print()
Dod.info_print()