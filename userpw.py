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
    pwd = raw_input('passwd: ')
    logt=time()
    db[name]=[pwd,logt]

def olduser(): 
    name=raw_input('login: ') 
    pwd=raw_input('passwd: ')
    if name in db:
        if pwd == db.get(name)[0]: 
            print 'welcome back',name 
            print 'You lasttime logged in at:',ctime(db[name][1])
            current=time()
            delta=current-db[name][1]
            if delta<=14400: #判断是否在4小时内
                print 'You already logged in 4 hours period!'

            else:
                logt=time()#获取当前时间 
                db[name][1]=logt #把密码和时间组成列表存到字典，共享一个键
        else: 
            print 'login incorrect'  

    else: 
        print 'login incorrect'

def deluser():
    Getuserpwd()
    c=raw_input('del a user,its name:')
    if c in db.keys():
        del db[c]
        print 'After del:'
        Getuserpwd()
    else:
        print 'Wrong choose!'

def Getuserpwd():
    if db:    
        for name in db:
            print 'name:',name,'pwd:',db[name][0]
    else:
        print 'No usr!'

def management():    
    prompt = """
(D)el a user
(G)et all user and pwd
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

            if choice not in 'gdq':
                print 'invalid menu option, try again'
            else:
                chosen = True

        if choice == 'q': done = 1
        if choice == 'd': deluser()
        if choice == 'g': Getuserpwd()


def showmenu():
    prompt = """
(N)ew User Login
(E)xisting User Login
(M)anagement
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

            if choice not in 'neqm':
                print 'invalid menu option, try again'
            else:
                chosen = True

        if choice == 'q': done = 1
        if choice == 'n': newuser()
        if choice == 'e': olduser()
        if choice == 'm': management()

if __name__ == '__main__':
    showmenu()
