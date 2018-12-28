print('Hello world!')
print('Hello Python!')
if True:
    print('True')
else:
    print('False')
print("-------------------------------------")
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
print(total)
print("-------------------------------------")
str = "RUNOOB"

print(str)        # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])     # 输出字符串第一个字符
print(str[2:])    # 输出从第三个开始的后的所有字符
print(str[2:5])   # 输出从第三个开始到第五个的字符
print(str * 2)    # 输出字符串两次
print(str+'你好啊')  #连接字符串

print("-------------------------------------")

print('hello\nmark')  # 使用反斜杠(\)+n转义特殊字符
print(r"hello\nMark") # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
print("-------------------------------------")

temp = input("\n\n按下 enter 键后退出。")
print(temp)

#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""


#在 python 用 import 或者 from...import 来导入相应的模块。
#将整个模块(somemodule)导入，格式为： import somemodule
#从某个模块中导入某个函数,格式为： from somemodule import somefunction
#从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
#将某个模块中的全部函数导入，格式为： from somemodule import *
import sys
for i in sys.argv:
    print (i)
print('\n python 路径为',sys.path)

##from sys import argv,path
#print("------------python from import------------------")
#print('path:'+sys.path)

