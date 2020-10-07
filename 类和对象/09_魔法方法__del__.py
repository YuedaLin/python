# 当删除对象时
class Washer():
    def __init__(self):
        # 添加实例属性
        self.width = 500
        self.height = 600
    def __del__(self):
        print(f"{self}对象已删除")

haier = Washer()