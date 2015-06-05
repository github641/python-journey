#!/usr/bin/env python

from time import time,ctime #导入模块
db = {}

def newuser():
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = raw_input('passwd: ')#用户名合格后，要求输入密码
    logt=time()#获取时间戳
    db[name]=[pwd,logt]#把密码和时间组成列表存到字典，共享一个键

def olduser(): 
    name=raw_input('login: ') 
    pwd=raw_input('passwd: ')
    if name in db:#检测是否是老用户
        if pwd == db.get(name)[0]: #获取老用户密码与输入密码比较
            print 'welcome back',name #显示欢迎信息
            print 'You lasttime logged in at:',ctime(db[name][1])
            #显示上次登录的时间戳
            current=time()#获取当前时间
            delta=current-db[name][1]#求上次登录与现在时间的时间差
            if delta<=14400: #判断是否在4小时内
                print 'You already logged in 4 hours period!'

            else:#若时间差不在四小时之内
                logt=time()#获取当前时间 
                db[name][1]=logt #把密码和时间组成列表存到字典，共享一个键，更新时间戳
        else: #密码错误
            print 'login incorrect'  

    else: #不是老用户
        print 'login incorrect'  

def showmenu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(Q)uit

Enter choice: """

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked: [%s]' % choice

            if choice not in 'neq':
                print 'invalid menu option, try again'
            else:
                chosen = True

        if choice == 'q': done = 1
        if choice == 'n': newuser()
        if choice == 'e': olduser()

if __name__ == '__main__':
    showmenu()
