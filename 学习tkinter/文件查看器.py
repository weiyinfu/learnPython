gCurrentDir = ''
import os
from tkinter import *

root = Tk()

Label(root, text='File operation demo').grid(row=0, column=0, columnspan=3)
Label(root, text='Directories').grid(row=1, column=0, stick=W)
Label(root, text='File').grid(row=1, column=1, stick=W)
Label(root, text='File Properities').grid(row=1, column=2, stick=W)

# 得到当前目录位置
gCurrentDir = os.getcwd()


def refreshDirs(lbDirs_, curDir):
    '''更新目录列表
    1.删除所有记录
    2.插入当前目录列表
    3.选中第一项
    '''
    lbDirs_.delete(0, END)
    lbDirs_.insert(0, '.')
    lbDirs_.insert(1, '..')
    for item in (os.listdir(curDir)):
        if os.path.isdir(curDir + (os.sep) + item):
            lbDirs_.insert(END, item)
    lbDirs_.selection_set(0)


def refreshFiles(lbFiles_, curDir):
    '''更新文件列表
    1.删除所有记录
    2.插入当前目录的文件列表
    3.选中第一项
    '''
    lbFiles_.delete(0, END)
    for item in (os.listdir(curDir)):
        if os.path.isfile(curDir + (os.sep) + item):
            lbFiles_.insert(END, item)
    lbFiles_.selection_set(0)


def changeDir(event):
    '''在目录ListBux双击时，
    1.改变当前路径，如果是'.'则不予处理，如果是'..'，去掉最后的项，
    2.同时更新文件列表
    3.更新文件显示属性'''
    global gCurrentDir
    sel = lbDirs.get(lbDirs.curselection())
    if sel == '.':
        return
    elif sel == '..':
        gCurrentDir = os.path.split(gCurrentDir)[0]
        print(gCurrentDir)
    else:
        gCurrentDir = gCurrentDir + os.sep + sel
        print(gCurrentDir)
    os.chdir(gCurrentDir)
    refreshDirs(lbDirs, gCurrentDir)
    refreshFiles(lbFiles, gCurrentDir)
    showProperties(event)


# 创建目录列表
lbDirs = Listbox(root)
refreshDirs(lbDirs, gCurrentDir)
lbDirs.grid(row=2, column=0, stick=W)
lbDirs.bind('<Double-Button-1>', changeDir)


def showProperties(event):
    '''用于显示文件的属性
    1.文件路径
    2.文件大小
    3.文件创建日期
    4.文件修改日期
    5.文件访问日期'''
    import time
    try:
        # 注意考虑当前目录没有文件的情况，这里使用异常处理，信息显示为空
        fn = gCurrentDir + os.sep + lbFiles.get(lbFiles.curselection())
        print('fn = ', fn)
        state = os.stat(fn)
        msg = ''
        msg = 'Location: ' + fn + ' '
        msg = msg + 'size:' + ('%d' % state[-4]) + ' '
        t = time.localtime(state[-1])
        msg = msg + 'create:' + ('%d/%d/%d %d:%d:%d' % (t[0], t[1], t[2], t[3], t[4], t[5])) + ' '
        t = time.localtime(state[-2])
        msg = msg + 'modify:' + ('%d/%d/%d %d:%d:%d' % (t[0], t[1], t[2], t[3], t[4], t[5])) + ' '
        t = time.localtime(state[-3])
        msg = msg + 'access:' + ('%d/%d/%d %d:%d:%d' % (t[0], t[1], t[2], t[3], t[4], t[5])) + ' '  # os.linesep

        lblProperities['text'] = msg
    except:
        msg = ''
        lblProperities['text'] = msg


# 创建文件列表
lbFiles = Listbox(root)
refreshFiles(lbFiles, gCurrentDir)
lbFiles.grid(row=2, column=1, stick=W)
lbFiles.bind('<Double-Button-1>', showProperties)

# 创建属性标签
lblProperities = Message(root)
showProperties(0)
lblProperities.grid(row=2, column=2)
root.mainloop()
