# -*- encoding:utf-8 -*-
from tkinter import *
from tkinter.ttk import *
import time

scale = 100


def create(root, button, max_task_num):
    top = Toplevel()
    top.title('票据生成进度')

    pb = Progressbar(top, length=200, mode="determinate", orient=HORIZONTAL)
    pb.pack(padx=10, pady=20)
    pb["maximum"] = max_task_num
    pb["value"] = 0

    button.configure(text="正在生成...", state=DISABLED)
    print("\n" * 2)
    print("执行开始".center(scale + 28, '-'))
    start = time.perf_counter()
    for i in range(max_task_num + 1):
        pb["value"] = i  # 每次更新1
        root.update()  # 更新画面

        # 以下为本地输出进度条
        a = '*' * i
        b = '.' * (max_task_num - i)
        c = (i / max_task_num) * 100
        t = time.perf_counter() - start
        print("\r任务进度:{:>3.0f}% [{}->{}]消耗时间:{:.2f}s".format(c, a, b, t), end="")
        # time.sleep(0.03)
        # 以上为本地输出进度条
    print("\n" + "执行结束".center(scale + 28, '-'))
    btn.configure(text="重启任务", state=NORMAL)
    top.destroy()