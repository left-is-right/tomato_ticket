import tkinter as tk
from UI.data_process_UI import DataProcessUI
from UI.elements_factory import ElementsFactory


class MainUI(object):

    def __init__(self):
        # 创建主窗口
        self.root_window = tk.Tk()
        self.root_window.geometry("1000x450")
        self.root_window.title('数据处理工具')
        self.elements_factory = ElementsFactory()
        self.data_process_ui = DataProcessUI(self.root_window)
        self.data_process_ui.create_UI()

        # 功能选择
        options_dict = {}
        options_dict["数据处理"] = self.choose_data_process
        options_dict["生成票样"] = self.choose_other
        self.elements_factory.make_select_element(self.root_window, [], "功能选择", 1, options_dict)

    def choose_data_process(self):
        print("选择")
        self.data_process_ui.display()

    def choose_other(self):
        self.data_process_ui.hide()

    def run(self):
        self.root_window.mainloop()



