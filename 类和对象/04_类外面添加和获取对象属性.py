# 属性就是特征
class Washer():
    def wash(self):
        print("能洗衣服")

haier = Washer()
# 添加属性：对象名.属性名 = 值
haier.width = 400
haier.height = 600

# 获取属性：对象名.属性名
print(f"洗衣机的宽度是{haier.width}")
print(f"洗衣机的高度是{haier.height}")