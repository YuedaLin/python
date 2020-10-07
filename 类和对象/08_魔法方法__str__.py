# 当使用print输出对象时，默认打印对象的内存地址，如果类定义了__str__方法，那么就会打印从这个方法中return的数据
class Washer():
    def __init__(self):
        # 添加实例属性
        self.width = 500
        self.height = 600

    def __str__(self):
        return "这是海尔洗衣机的使用说明书"

haier = Washer()
print(haier)