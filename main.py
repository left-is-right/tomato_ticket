# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 08:28:41 2024

@author: 勾皓亮
"""

import pandas as pd
import tkinter as tk
from tkinter import messagebox, Toplevel, filedialog, ttk, HORIZONTAL, DISABLED, NORMAL
from tkinter.ttk import *
from pathlib import Path
from decimal import *
from server.DataProcessServer import dataProcessServer
from server.TicketMakeServer import tickMakeServer
from docx import Document
from docx.shared import Cm, Pt
from utils.judge_number import judge_int
import _tkinter
import time

"""
主界面生成
"""

def mainGUI():

    # 一级组件字典
    elements_dict = {}

    def selectMainElements(selectedModule):
        closeSecondaryElements()
        allKeys = elements_dict.keys()
        for module in allKeys:
            if module == selectedModule:
                for element in elements_dict[module]:
                    element.grid()
            else:
                for element in elements_dict[module]:
                    element.grid_remove()

    # 关闭所有次级组件
    def closeSecondaryElements():
        for elements_list in elements_dict.values():
            for element in elements_list:
                element.grid_remove()

    # 创建主窗口
    root_window = tk.Tk()
    root_window.geometry("650x200")
    # comp_name = "内蒙古昶锦商贸有限公司"
    comp_name = "鄂尔多斯市科丰农业科技有限责任公司"
    # comp_name = "内蒙古伍星食品有限责任公司"
    root_window.title('数据处理及票据生成工具（{}）'.format(comp_name))

    # 组件列表
    selectFun = tk.Label(root_window, text="功能选择")
    selectFun.grid(row=0, column=0)
    fun = tk.StringVar()

    # 定义数据文件的选择路径
    def getFilePath(path):
        path_ = filedialog.askopenfilename()
        if path_ == "":
            path.get()
        else:
            path.set(path_)

    def getDirctoryPath(path, file_name):
        path_ = filedialog.askdirectory()
        if path_ == "":
            path.get()
        else:
            path_ = path_.replace("/", "\\") + '\\' + file_name
            path.set(path_)

    '''
        数据处理模块
    '''
    data_process_elements_list = []
    data_process = ttk.Radiobutton(root_window, text='数据处理', variable=fun, value='数据处理',
                                   command=lambda: selectMainElements('data_process'))
    data_process.grid(row=0, column=1)

    # 文件输入
    # 定义路径动态变量
    input_path = tk.StringVar()  # 详情文件路径
    input_path.set(str(Path.cwd()))  # 默认当前目录
    output_path = tk.StringVar()  # 结果文件路径
    output_path.set(str(Path.cwd()) + '\\数据处理结果.xlsx')  # 默认当前目录

    # 输入文件
    inputPathLabel = tk.Label(root_window, text="数据输入文件")
    inputPathLabel.grid(row=1, column=0)
    inputPathLabel.grid_remove()
    data_process_elements_list.append(inputPathLabel)

    inputPathEntry = tk.Entry(root_window, textvariable=input_path, state="readonly")
    inputPathEntry.grid(row=1, column=1, ipadx=100, columnspan=2)
    inputPathEntry.grid_remove()
    data_process_elements_list.append(inputPathEntry)

    inputPathButton = tk.Button(root_window, text="路径选择", command=lambda: getFilePath(input_path))
    inputPathButton.grid(row=1, column=3)
    inputPathButton.grid_remove()
    data_process_elements_list.append(inputPathButton)

    # 输出文件路径
    outputPathLabel = tk.Label(root_window, text="结果输出路径")
    outputPathLabel.grid(row=2, column=0)
    outputPathLabel.grid_remove()
    data_process_elements_list.append(outputPathLabel)

    outputPathEntry = tk.Entry(root_window, textvariable=output_path, state="readonly")
    outputPathEntry.grid(row=2, column=1, ipadx=100, columnspan=2)
    outputPathEntry.grid_remove()
    data_process_elements_list.append(outputPathEntry)

    outputPathButton = tk.Button(root_window, text="路径选择", command=lambda: getDirctoryPath(output_path, "数据处理结果.xlsx"))
    outputPathButton.grid(row=2, column=3)
    outputPathButton.grid_remove()
    data_process_elements_list.append(outputPathButton)


    # 毛重系数
    weight_coe_var = tk.StringVar()
    weight_coe_var.set(str(1))  # 默认值为1
    weightLabel = tk.Label(root_window, text="毛重系数")
    weightLabel.grid(row=3, column=0)
    weightLabel.grid_remove()
    data_process_elements_list.append(weightLabel)
    weightEntry = tk.Entry(root_window, textvariable=weight_coe_var)
    weightEntry.grid(row=3, column=1)
    weightEntry.grid_remove()
    data_process_elements_list.append(weightEntry)

    # 预设单价
    price_coe_var = tk.StringVar()
    price_coe_var.set(str(1))  # 默认值为1
    priceLabel = tk.Label(root_window, text="预设单价")
    priceLabel.grid(row=3, column=2)
    priceLabel.grid_remove()
    data_process_elements_list.append(priceLabel)
    priceEntry = tk.Entry(root_window, textvariable=price_coe_var)
    priceEntry.grid(row=3, column=3)
    priceEntry.grid_remove()
    data_process_elements_list.append(priceEntry)

    # 设置按键
    # 定义按键函数
    def startCalc():
        try:
            ori_data = pd.read_excel(str(input_path.get()), dtype=str)
        except Exception:
            messagebox.showinfo('提示', '输入文件必须为xlsx类型文件！')
            return

        try:
            weight_coe = Decimal(weight_coe_var.get())
        except Exception:
            messagebox.showinfo('提示', '毛重系数必须为整数或小数！')
            return

        try:
            price = Decimal(price_coe_var.get())
        except Exception:
            messagebox.showinfo('提示', '预设单价必须为整数或小数！')
            return

        output_file = output_path.get()
        status = dataProcessServer(ori_data, output_file, weight_coe, price)
        if status == 0:
            messagebox.showinfo('提示', '计算完成')
            # root_window.destroy()
        elif status == 1:
            messagebox.showinfo('提示',
                                '请检查输入数据文件是否包含以下列名：\n 流水号 \n 毛重 \n 皮重 \n 净重 \n 单价 \n 金额')
        elif status == 2:
            messagebox.showinfo('提示', "计算失败，请检查结果表是否正在打开")
            # root_window.destroy()

    start_button = tk.Button(root_window, text="生成数据", command=startCalc)
    start_button.grid(row=4, column=1)
    start_button.grid_remove()
    data_process_elements_list.append(start_button)

    elements_dict['data_process'] = data_process_elements_list

    '''
    票据生成
    '''
    ticket_make_elements_list = []
    ticket_make = ttk.Radiobutton(root_window, text='票据生成', variable=fun, value='票据生成',
                                   command=lambda: selectMainElements('ticket_make'))
    ticket_make.grid(row=0, column=2)

    # 输入文件
    ticket_input_path = tk.StringVar()  # 详情文件路径
    ticket_input_path.set(str(Path.cwd()))  # 默认当前目录
    ticketInputPathLabel = tk.Label(root_window, text="数据输入文件")
    ticketInputPathLabel.grid(row=1, column=0)
    ticketInputPathLabel.grid_remove()
    ticket_make_elements_list.append(ticketInputPathLabel)

    ticketInputPathEntry = tk.Entry(root_window, textvariable=ticket_input_path, state="readonly")
    ticketInputPathEntry.grid(row=1, column=1, ipadx=100, columnspan=2)
    ticketInputPathEntry.grid_remove()
    ticket_make_elements_list.append(ticketInputPathEntry)

    ticketInputPathButton = tk.Button(root_window, text="路径选择", command=lambda: getFilePath(ticket_input_path))
    ticketInputPathButton.grid(row=1, column=3)
    ticketInputPathButton.grid_remove()
    ticket_make_elements_list.append(ticketInputPathButton)

    # 输出文件路径
    ticket_output_path = tk.StringVar()  # 详情文件路径
    ticket_output_path.set(str(Path.cwd()) + "\\票据打印.docx")  # 默认当前目录
    ticketOutputPathLabel = tk.Label(root_window, text="结果输出路径")
    ticketOutputPathLabel.grid(row=2, column=0)
    ticketOutputPathLabel.grid_remove()
    ticket_make_elements_list.append(ticketOutputPathLabel)

    ticketOutputPathEntry = tk.Entry(root_window, textvariable=ticket_output_path, state="readonly")
    ticketOutputPathEntry.grid(row=2, column=1, ipadx=100, columnspan=2)
    ticketOutputPathEntry.grid_remove()
    ticket_make_elements_list.append(ticketOutputPathEntry)

    ticketOutputPathButton = tk.Button(root_window, text="路径选择", command=lambda: getDirctoryPath(ticket_output_path, "票据打印.docx"))
    ticketOutputPathButton.grid(row=2, column=3)
    ticketOutputPathButton.grid_remove()
    ticket_make_elements_list.append(ticketOutputPathButton)

    # 流水号范围
    min_id_var = tk.StringVar()
    minIdLabel = tk.Label(root_window, text="最小流水号（包含）")
    minIdLabel.grid(row=3, column=0)
    minIdLabel.grid_remove()
    ticket_make_elements_list.append(minIdLabel)
    minIdEntry = tk.Entry(root_window, textvariable=min_id_var, validate='key',
                          validatecommand=(root_window.register(judge_int), '%P'))
    minIdEntry.grid(row=3, column=1)
    minIdEntry.grid_remove()
    ticket_make_elements_list.append(minIdEntry)

    max_id_var = tk.StringVar()
    maxIdLabel = tk.Label(root_window, text="最大流水号（包含）")
    maxIdLabel.grid(row=3, column=2)
    maxIdLabel.grid_remove()
    ticket_make_elements_list.append(maxIdLabel)
    maxIdEntry = tk.Entry(root_window, textvariable=max_id_var, validate='key',
                          validatecommand=(root_window.register(judge_int), '%P'))
    maxIdEntry.grid(row=3, column=3)
    maxIdEntry.grid_remove()
    ticket_make_elements_list.append(maxIdEntry)

    # 登记人
    registrant_var = tk.StringVar()
    registrantLabel = tk.Label(root_window, text="登记人")
    registrantLabel.grid(row=4, column=0)
    registrantLabel.grid_remove()
    ticket_make_elements_list.append(registrantLabel)
    registrantEntry = tk.Entry(root_window, textvariable=registrant_var)
    registrantEntry.grid(row=4, column=1)
    registrantEntry.grid_remove()
    ticket_make_elements_list.append(registrantEntry)

    # 设置按键
    # 定义按键函数
    def startMake():
        try:
            data = pd.read_excel(str(ticket_input_path.get()), dtype=str)
        except Exception:
            messagebox.showinfo('提示', '输入文件必须为xlsx类型文件！')
            return

        try:
            min_id = int(min_id_var.get())
        except ValueError:
            min_id = 0
        try:
            max_id = int(max_id_var.get())
        except ValueError:
            max_id = 9223372036854775807

        try:
            data = data[['合同号', '回皮时间', '流水号', '农户姓名', '车牌号', '地址', '车辆类型', '毛重', '净重',
                         '单价', '金额', '重磅员']]
        except KeyError:
            messagebox.showinfo('提示', '检查输入文件是否包含以下列名：\n合同号, 回皮时间, 流水号, 农户姓名, 车牌号, 地址, 车辆类型, 毛重, 净重, 单价, 金额, 重磅员')
            return

        mask = data['流水号'].str.contains('^[0-9]*$')
        data = data[mask]
        data['流水号（整数）'] = data['流水号'].astype(int)
        data = data[(data['流水号（整数）'] >= min_id) & (data['流水号（整数）'] <= max_id)].reset_index(drop=True)
        data.drop(columns=['流水号（整数）'], inplace=True)

        data['登记人'] = str(registrant_var.get())

        doc = Document()
        default_section = doc.sections[0]
        # 可直接修改宽度和高度，即纸张大小改为自定义（A4纸是21 * 29.7）
        default_section.page_width = Cm(21)
        default_section.page_height = Cm(29.7)

        # 修改页边距
        default_section.top_margin = Pt(26)  # 1CM = 28.35PT
        default_section.right_margin = Cm(1.2)
        default_section.bottom_margin = Pt(26)
        default_section.left_margin = Cm(1.2)

        # 弹出进度条
        top = Toplevel()
        top.title('票据生成进度')

        pb = Progressbar(top, length=200, mode="determinate", orient=HORIZONTAL)
        pb.pack(padx=10, pady=20)
        pb["maximum"] = len(data)
        pb["value"] = 0

        start = time.perf_counter()
        pb_text = tk.StringVar()
        pb_label = tk.Label(top, textvariable=pb_text)
        pb_label.pack()

        make_button.configure(text="正在生成...", state=DISABLED)
        for idx, row in data.iterrows():
            try:
                tickMakeServer(doc, row, comp_name)
                pb["value"] = idx  # 每次更新1
                t = time.perf_counter() - start
                pb_text.set("任务进度:{}/{}  消耗时间:{:.2f}s".format(idx, len(data), t))
                top.update()
                # print("完成第{}张票据生成".format(idx + 1))
                if (idx + 1) % 3 != 0:
                    gap = doc.add_paragraph(
                        '------------------------------------------------------------------------------------------------------------------------------------------------')
                    gap.paragraph_format.space_before = Pt(26)  # 段前10磅
                    gap.paragraph_format.space_after = Pt(26)  # 段后10磅
                else:
                    doc.add_page_break()
            except _tkinter.TclError:
                top.destroy()
                make_button.configure(text="生成票据", state=NORMAL)
                return
        doc.save(str(ticket_output_path.get()))
        top.destroy()
        make_button.configure(text="生成票据", state=NORMAL)

    make_button = tk.Button(root_window, text="生成票据", command=startMake)
    make_button.grid(row=5, column=1)
    make_button.grid_remove()
    ticket_make_elements_list.append(make_button)

    tipsLabel = tk.Label(root_window, text="最小流水号为空即为从头开始，最大流水号为空即为直到最后一条")
    tipsLabel.grid(row=6, column=0, columnspan=4)
    tipsLabel.grid_remove()
    ticket_make_elements_list.append(tipsLabel)

    elements_dict['ticket_make'] = ticket_make_elements_list

    return root_window


if __name__ == '__main__':
    root_window = mainGUI()
    root_window.mainloop()
