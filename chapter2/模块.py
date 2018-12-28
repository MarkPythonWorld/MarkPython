# 模块
import sys
print('命令行参数如下：')
for i in sys.argv:
   print (i)

print('\n\nPython路径为：',sys.path,'\n')


# 导入模块
import support

# 现在可以调用模块里面的函数
support.print_funv("Mark")


# 函数
import feibo
print(dir(feibo))