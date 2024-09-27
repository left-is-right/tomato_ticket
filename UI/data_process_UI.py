import tkinter as tk
from tkinter import filedialog
from pathlib import Path
from UI.elements_factory import ElementsFactory
from server.DataProcessServer import dataProcessServer

class DataProcessUI(object):

    elements_list = []

    def __init__(self, root_window):
        self.root_window = root_window

    def create_UI(self):
        elements_maker = ElementsFactory()
        # 输入文件选取
        input_file = elements_maker.make_path_element(self.root_window, self.elements_list, "选择输入文件", row=1)
        # 输出文件选择
        output_file = elements_maker.make_path_element(self.root_window, self.elements_list, "选择结果文件路径", row=2,
                                                       file_name="数据处理结果文件.xlsx")
        # 设置输入系数
        weight_coe = elements_maker.make_input_element(self.root_window, self.elements_list, "毛重系数", row=3, column=0)
        price_coe = elements_maker.make_input_element(self.root_window, self.elements_list, "单价系数", row=3, column=2)
        # 设置启动按键
        elements_maker.make_button_element(self.root_window, self.elements_list, "开始计算",
                                           dataProcessServer, 4, 1)
        print(self.elements_list)

    def display(self):
        for element in self.elements_list:
            print("显示" + element)
            element.grid()

    def hide(self):
        for element in self.elements_list:
            element.grid_remove()