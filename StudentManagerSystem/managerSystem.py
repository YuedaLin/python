# 需求：系统循环使用，用户输入不同的功能序号执行不同的功能
"""
步骤：
一、.定义程序入口函数
    1.加载数据
    2.显示功能菜单
    3.用户输入功能序号
    4.根据用户输入的功能序号执行不同的功能
二、.定义系统功能函数，添加、删除学院等
"""

from student import  *
class StudentManager():
    def __init__(self):
        # 存储数据所用的列表
        self.student_list = []

    # 一、程序入口函数，启动程序后执行的函数
    def run(self):
        # 1.加载学员信息
        self.load_student()

        while True:
            # 2.显示功能菜单
            self.show_menu()

            # 3.用户输入功能序号
            menu_num = int(input(('请输入您需要的功能序号：')))

            # 4.根据用户输入的徐奥执行不同的功能
            if menu_num == 1:
                # 添加学学员
                self.add_student()

            elif menu_num == 2:
                # 删除学员
                self.del_student()

            elif menu_num == 3:
                # 修改学员信息
                self.modify_student()

            elif menu_num == 4:
                # 查询学员信息
                self.search_student()

            elif menu_num == 5:
                # 显示所有学员信息
                self.show_student()
            elif menu_num == 6:
                # 保存学员信息
                self.save_student()

            elif menu_num == 7:
                # 退出系统
                break

    # 二、系统功能函数
    # 2.1 显示功能菜单 -- 打印序号的功能对应关系 -- 静态方法
    @staticmethod
    def show_menu():
        print('请选择如下功能：')
        print('1.添加学员')
        print('2.删除学员')
        print('3.修改学员信息')
        print('4.查询学员信息')
        print('5.显示所有学员信息')
        print('6.保存学员信息')
        print('7.推出系统')
    # 2.2添加学员
    def add_student(self):
        # 1.用户输入姓名，性别，手机号
        name = input('请输入您的姓名：')
        gender = input('请输入您的性别：')
        tel = input('请输入您的手机号码：')

        # 2.创建学员对象 --类在student文件里面，先导入student模块，再创建对象
        student = Student(name, gender, tel)

        # 3.将对象添加到学员列表
        self.student_list.append(student)

        # 测试是否添加成功
        print(self.student_list)
        print(student)

    # 2.3删除学员：删除指定姓名学员
    def del_student(self):
        # 1.用户输入目标学员姓名
        del_name = input('请输入要删除的学员姓名：')

        # 2.如果目标学院存在则删除，否则提示学员不存在
        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                break
        else:
            print('查无此人')

        # 打印学员列表，验证删除功能
        print(self.student_list)

    # 2.4修改学员信息
    def modify_student(self):
        # 1.输入要修改信息的学员姓名
        modify_name = input('请输入您要修改的学员的姓名：')

        # 2.遍历列表，有则改，无则提示
        for i in self.student_list:
            if i.name == modify_name:
                i.name = input('请输入学员姓名：')
                i.gender = input('请输入学员性别：')
                i.tel = input('请输入学员手机号：')
                print(f'修改该学员信息成功，姓名：{i.name}，性别{i.gender}，手机号{i.tel}')
                break
        else:
            print('查无此人')

        # 打印学员列表，验证修改功能
        print(self.student_list)

    # 2.5查询学员信息
    def search_student(self):
        search_name = input('请输入您要查询的学员姓名：')

        for i in self.student_list:
            if i.name == search_name:
                print(f'该学员的姓名：{i.name}，性别{i.gender}，手机号{i.tel}')
                break
        else:
            print('查无此人')

    # 2.6显示所有学员信息
    def show_student(self):
        # 打印表头
        print('姓名\t性别\t手机号')

        # 打印学员数据
        for i in self.student_list:
            print(f'{i.name}\t{i.gender}\t{i.tel}')

    # 2.7保存学员信息
    def save_student(self):
        # 1.打开文件
        f = open('student.data', 'w')

        # 2.文件写入学员数据
        # 注意1：文件写入的数据不能是学员对象的内存的地址，需要把学员数据转换成列表字典数据再存储
        new_list = [i.__dict__ for i in self.student_list]
        # [{'name': 'aa', 'gender': 'nv', 'tel': '111'}]

        # 注意2.文件内数据要求为字符串类型，故需要先转换数据类型为字符串才能文件写入数据
        f.write(str(new_list))

        # 3.关闭文件
        f.close()

    # 2.8加载学员信息
    def load_student(self):
        # 1.打开文件
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            # 2.读取数据：文件读取的数据是字符串，还原列表类型：[{}] 转换[学员对象]
            data = f.read() # 字符串
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['gender'], i['tel']) for i in new_list]

        finally:
            # 3.关闭文件
            f.close()

