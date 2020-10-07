# 一般定义函数名为get_xx用来获取私有属性，定义set_xx用来修改私有属性值
class Master():
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')
# 定义学校类
class School():
    def __init__(self):
        self.kongfu = '[学校的煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

class Prentice(Master, School):
    def __init__(self):
        self.kongfu = '[独创的煎饼果子配方]'
        # 设置私有属性
        self.__money = 200000

    # 获取私有属性
    def get_money(self):
        return self.__money

    # 修改私有属性
    def set_money(self):
        self.__money = 500

    # 定义私有方法
    def __info_print(self):
        print('这是私有方法')

    # 如果先调用了父类的属性和方法，父类属性会覆盖子类属性，所以在调用属性之前，先调用自己子类的初始化
    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作煎饼果子')

    # 调用父类方法，但是为了保证调用到的是父类的属性，必须在调用方法前调用父类的初始化
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

# 徒孙类
class Tusun(Prentice):
    pass

xiaoqiu = Tusun()
print(xiaoqiu.get_money())
xiaoqiu.set_money()
print(xiaoqiu.get_money())