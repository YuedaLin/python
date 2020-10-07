# 1.师傅类
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

# 2.徒弟类，继承师傅类和学校类
class Prentice(Master, School):
    def __init__(self):
        self.kongfu = '[独创的煎饼果子配方]'

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

# 3.用徒孙弟类创建对象
xiaoqiu = Tusun()
xiaoqiu.make_cake()
xiaoqiu.make_master_cake()
xiaoqiu.make_school_cake()

# 4.查看继承顺序
print(Tusun.__mro__)