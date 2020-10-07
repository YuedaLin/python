# 在python中，抛出自定义异常的语法为：raise 异常类对象
# 1.自定义异常类，继承Exception，魔法方法为init和str（设置异常信息）
class ShortInputError(Exception):
    def __init__(self, length, min_len):
        self.length = length
        self.min_len = min_len

    # 设置抛出异常的描述信息
    def __str__(self):
        return f'你输入的密码长度为{self.length}, 不能少于{self.min_len}个字符'

def main():
    # 2.抛出异常：尝试执行，用户输入密码，如果长度小于3，抛出异常
    try:
        con = input('请输入密码：')
        if len(con) < 3:
            # 抛出异常类创建的对象
            raise ShortInputError(len(con), 3)
    # 3.捕获该异常
    except Exception as result:
        print(result)
    else:
        print('密码已经输入完成')

main()