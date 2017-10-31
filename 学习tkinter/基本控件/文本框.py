import tkinter

root = tkinter.Tk()

entry1 = tkinter.Entry(root, show='*')
entry1.pack()

entry2 = tkinter.Entry(root, show='#', width='50')
entry2.pack()

entry3 = tkinter.Entry(root, bg='red', fg='blue')
entry3.pack()

entry4 = tkinter.Entry(root, selectbackground='red', \
                       selectforeground='gray')
entry4.pack()

entry5 = tkinter.Entry(root, state=tkinter.DISABLED)
entry5.pack()

edit1 = tkinter.Text(root, selectbackground='red',
                     selectforeground='gray')
edit1.pack()
e = tkinter.StringVar()
entry = tkinter.Entry(root, textvariable=e)
e.set('input your text here')
entry.pack()
entry['state'] = 'readonly'
# 密码框
# 分别使用*#$显示输入的文本内容
for mask in ['*', '#', '$']:
    e = tkinter.StringVar()
    entry = tkinter.Entry(root, textvariable=e)
    e.set('password')
    entry.pack()
    entry['show'] = mask
# validate
e = tkinter.StringVar()


def validateText(contents):
    print(contents)
    return contents.isalnum()


entry = tkinter.Entry(root, validate='key', textvariable=e, validatecommand=validateText)
entry.pack()
root.mainloop()
