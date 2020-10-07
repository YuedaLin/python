# 需求1：尝试打开文件，文件存在读取内容，不存在提示用户
# 需求2：读取内容：循环读取，当无内容时推出循环，如哦用户意外终止，提示用户已经被意外终止
import time
try:
    f = open('test.txt')

    try:
        while True:
            content = f.readline()
            # print(len(content))
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        # 在命令提示符按下ctrl+c结束终止的健
        print('程序被终止')

except:
    f = open('该文件不存在')