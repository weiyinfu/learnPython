import tkinter

root = tkinter.Tk()

lbl1 = tkinter.Label(root, anchor=tkinter.E,
                     bg='blue', fg='red', text='Python', width=30, height=5)
lbl1.pack()

lbl2 = tkinter.Label(root, text='Python GUI\nTkinter',
                     justify=tkinter.LEFT, width=30, height=5)
lbl2.pack()

lbl3 = tkinter.Label(root, text='Python GUI\nTkinter',
                     justify=tkinter.RIGHT, width=30, height=5)
lbl3.pack()

lbl4 = tkinter.Label(root, text='Python GUI\nTkinter',
                     justify=tkinter.CENTER, width=30, height=5)
lbl4.pack()
label5 = tkinter.Label(root, bitmap='error', text="hhaa", compound="top")
# 上面的代码使用了内置位图error
label5.pack()

tkinter.Label(root, text='welcome to jcodeer.cublog.cn', bg='yellow', width=40, height=3, wraplength=80,
              justify='left').pack()
# 居中对齐，文本居左
tkinter.Label(root, text='welcome to jcodeer.cublog.cn', bg='red', width=40, height=3, wraplength=80, anchor='w').pack()
# 居中对齐，文本居右
tkinter.Label(root, text='welcome to jcodeer.cublog.cn', bg='blue', width=40, height=3, wraplength=80,
              anchor='n').pack()

root.mainloop()
"""
其他可用的位图：
    * error
    * hourglass
    * info
    * questhead
    * question
    * warning
    * gray12
    * gray25
    * gray50
    * gray75
若要查看各自的效果，可以使用相应的名称将bitmpa = 'error'替换。
据说还可以使用自己指定的位图文件,网上找了一下，格式如下：
    Label(root, bitmap="@/path/bitmapname")
不过我试了一下，从来没有成功过，我已经将位图该为单色的了:(

另：还有的网上的文章说明如何使用PhotoImage和BitmapImage显示bmp或gif文件，提到一点
防止图像文件被python自动回收(garbage collected)，应将bmp或gif放到全局(global)或实体
(instance)中，使用如下两种方法，仍未奏效：

compound:    指定文本(text)与图像(bitmap/image)是如何在Label上显示，缺省为None，
当指定image/bitmap时，文本(text)将被覆盖，只显示图像了。可以使用的值：
    left：    图像居左
    right:    图像居右
    top：    图像居上
    bottom：图像居下
    center：文字覆盖在图像上
bitmap/image:
    显示在Label上的图像
text:
    显示在Label上的文本
label = Label(root,text = 'Error',compound = 'left',bitmap = 'error')
"""
