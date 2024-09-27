# -*- encoding:utf-8 -*-
from tkinter import *
from tkinter.ttk import *
import time
import pandas as pd
import _tkinter

data = pd.read_excel("D:/私人/数据处理/19.xlsx", dtype=str)

print(data.columns)
data.rename(columns=lambda x: x.replace(' ', ''), inplace=True)
print(data.columns)
#
# scale = 100
#
# root = Tk()
# root.title("任务进度可视化")
#
#
# def create():
#     top = Toplevel()
#     top.title('Python')
#
#     pb = Progressbar(top, length=200, mode="determinate", orient=HORIZONTAL)
#     pb.pack(padx=10, pady=20)
#     pb["maximum"] = 100
#     pb["value"] = 0
#
#     btn.configure(text="系统忙碌中...", state=DISABLED)
#     print("\n" * 2)
#     print("执行开始".center(scale + 28, '-'))
#     start = time.perf_counter()
#     for i in range(scale + 1):
#         try:
#             pb["value"] = i  # 每次更新1
#             top.update()  # 更新画面
#             a = '*' * i
#             b = '.' * (scale - i)
#             c = (i / scale) * 100
#             t = time.perf_counter() - start
#             print("\r任务进度:{:>3.0f}% [{}->{}]消耗时间:{:.2f}s".format(c, a, b, t), end="")
#             time.sleep(0.03)
#         except _tkinter.TclError as e:
#             # print(e)
#             print("任务中断")
#             btn.configure(text="重启任务", state=NORMAL)
#             return
#     print("\n" + "执行结束".center(scale + 28, '-'))
#     btn.configure(text="重启任务", state=NORMAL)
#     top.destroy()
#
#
# btn = Button(root, text="启动任务", command=create)
# btn.pack()
#
#
# label = Label(root, text="这是一个标签")
# label.grid(row=2, column=0)
#
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)
#
# root.mainloop()
#
# root.mainloop()