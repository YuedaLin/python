# 目标：定义init魔法方法设置初始化属性，并访问调用
class Washer():
    def __init__(self):
        # 添加实例属性
        self.width = 500
        self.height = 600

    def wash(self): # 添加实例方法，访问实例属性
        print(f"洗衣机的宽度是{self.width}")
        print(f"洗衣机的高度是{self.height}")

haier = Washer()

haier.wash()