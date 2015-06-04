
def makeTextFile():
    import os
    ls = os.linesep

    # get filename
    while True:
        fname = raw_input('Enter file name: ')
        if os.path.exists(fname):
            print"*** ERROR: '%s' already exists" % fname
        else:
            break

    # get file content (text) lines
    all = []
    print "\nEnter lines ('.' by itself to quit).\n"

    # loop until user terminates input
    while True:
        entry = raw_input('> ')
        if entry == '.':
            break
        else:
            all.append(entry)

    # write lines to file with proper line-ending
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()
    print 'DONE!'
    print call()

def readTextFile():
    # get filename
    fname = raw_input('Enter file name: ')
    print

    # attempt to open file for reading
    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print"*** file open error:", e
    else:
        # display contents to the screen
        for eachLine in fobj:
            print eachLine,
        fobj.close()
    print call()
def call():
    t=raw_input("Input 'm' for make,'r' for read:")
    if t=='r':
        readTextFile()
    elif t=='m':
        makeTextFile()
    else:
        t=raw_input("Wrong answer!Input 'm' for make,'r' for read:")
    
print call()
