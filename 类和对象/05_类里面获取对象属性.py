# 属性就是特征
class Washer():
    def wash(self):
        # 类里面获取实例属性:self.属性名
        print(f"洗衣机的宽度是{self.width}")
        print(f"洗衣机的高度是{self.height}")

haier = Washer()
# 添加属性：对象名.属性名 = 值
haier.width = 400
haier.height = 600

haier.wash()