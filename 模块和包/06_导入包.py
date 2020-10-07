# 方法一
import mypackage.my_module1
mypackage.my_module1.info_print()

# 方法二：必须在__init__.py文件中添加__all__=[],控制允许导入的模块列表
from mypackage import *
my_module2.info_print()