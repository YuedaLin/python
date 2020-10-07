# finally表示的是无论是否异常都要执行的代码，例如关闭文件
try:
    f = open('test.txt', 'r')

except Exception as result:
    f = open('test.txt', 'w')
else:
    print('没有异常')
finally:
    f.close()