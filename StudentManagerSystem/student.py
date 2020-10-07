# 需求：
# 学员信息包括：姓名、性别、手机号码
# 添加__str__魔法方法，方便查看学员对象信息

class Student():
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name}， {self.gender}, {self.tel}'

# 测试代码
# aa = Student('小红','女',1110)
# print(aa)