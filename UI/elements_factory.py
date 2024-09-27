import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from pathlib import Path


class ElementsFactory(object):

    def make_path_element(self, root_window, elements_list, label, row, file_name=""):
        """
        生成文件输入组件，生成label，path，button三个元素
        :param root_window:
        :param elements_list:
        :param label:
        :param row:
        :return:
        """
        # 文件路径选择
        getFilePath = tk.StringVar()
        getFilePath.set(str(Path.cwd()))
        getFilePathLabel = tk.Label(root_window, text=label)
        getFilePathLabel.grid(row=row)
        getFilePathLabel.grid_remove()
        elements_list.append(getFilePathLabel)

        getFilePathEntry = tk.Entry(root_window, textvariable=getFilePath, state="readonly")
        getFilePathEntry.grid(row=row, column=1, ipadx=200, columnspan=2)
        getFilePathEntry.grid_remove()
        elements_list.append(getFilePathEntry)

        if file_name == "":
            getFilePathButton = tk.Button(root_window, text="路径选择", command=lambda: self.getFilePath(getFilePath))
        else:
            getFilePathButton = tk.Button(root_window, text="路径选择", command=lambda: self.getDirctoryPath(getFilePath, file_name))
        getFilePathButton.grid(row=row, column=3)
        getFilePathButton.grid_remove()
        elements_list.append(getFilePathButton)

        return getFilePath

    def make_button_element(self, root_window, elements_list, button_text, button_fun, row, column):
        button = tk.Button(root_window, text=button_text, command=lambda: button_fun)
        button.grid(row=row, column=column)
        button.grid_remove()
        elements_list.append(button)

    def make_input_element(self, root_window, elements_list, label, row, column):
        inputLabel = tk.Label(root_window, text=label)
        inputLabel.grid(row=row, column=column)
        inputLabel.grid_remove()
        elements_list.append(inputLabel)

        inputEntry = tk.Entry(root_window)
        inputEntry.grid(row=row, column=column+1)
        inputEntry.grid_remove()
        elements_list.append(inputEntry)

        return inputEntry

    def make_select_element(self, root_window, elements_list, label, row, options_dict, is_hide=False):
        selectLabel = tk.Label(root_window, text=label)
        col = 0
        selectLabel.grid(row=row, column=col)
        fun = tk.StringVar()
        print(options_dict)
        for key, value in options_dict.items():
            col = col + 1
            option = ttk.Radiobutton(root_window, text=key, variable=fun, value=key,
                                     command=lambda: value)
            option.grid(row=row, column=col)
            if is_hide:
                option.grid_remove()
            elements_list.append(option)

        return fun


    # 定义数据文件的选择路径
    def getFilePath(self, path):
        path_ = filedialog.askopenfilename()
        if path_ == "":
            path.get()
        else:
            path.set(path_)

    def getDirctoryPath(self, path, file_name):
        path_ = filedialog.askdirectory()
        if path_ == "":
            path.get()
        else:
            path_ = path_.replace("/", "\\") + '\\' + file_name
            path.set(path_)