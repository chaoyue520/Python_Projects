# os.system的结果只是命令执行结果的返回值,执行成功为0:
# os.popen就可以读出执行的内容,popen返回的是file read的对象,对其进行读取使用read(),就可看到执行的输出:

## os.system()
a=os.system('ls')

#执行a，输出0表示执行成功
a

## os.popen()
b=os.popen('ls')

#通过read()函数即可看到执行的输出文件
b.read()

