#!/usr/bin/env python

#UNIX启动行
import string

#导入string模块
while 1:

    #循环条件，一直为真，一直循环直到break
    num_str = raw_input('Enter a number: ')

    #用户输入一个数字保存起来
    try:
        #异常检测
        num_num = string.atoi(num_str)

        #locale.atoi(string) 
Converts a string to an integer.

        break

    #转换完毕，跳出
    except ValueError:
        print "invalid input... try again"

#报错
fac_list = range(1, num_num+1)
print "BEFORE:", `fac_list`

#
i = 0
t=fac_list
#创建变量i赋初值为0
while i < len(t):

    #设定循环条件.只想到讲过要遍历副本，修改正主。这时用来将小于他且不能被他整除的所有数输出。
    if num_num % t[i] == 0:
        del fac_list[i]

    #
    i = i+1

#不知道还有什么bug。输入6、20、12、30不会死循环了。
print "AFTER:", `fac_list`  
