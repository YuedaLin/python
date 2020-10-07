# 1.导入managerSystem模块
from managerSystem import *

# 2.启动学员管理系统 --创建对象并调用run方法
if __name__ == '__main__':
    student_manager = StudentManager()

    student_manager.run()