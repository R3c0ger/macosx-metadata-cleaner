#!usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tkinter import messagebox, Tk


def delete_macos_files(directory):
    """
    在指定目录及其子目录中查找并删除 .DS_Store 和 __MACOSX 文件夹

    :param directory: 要查找的目录
    :return: 删除的文件列表
    :rtype: list[str]
    """
    deleted_files = []
    for root, dirs, files in os.walk(directory):
        # 删除 .DS_Store 文件
        for file in files:
            if file == '.DS_Store':
                file_path = os.path.join(root, file)
                os.remove(file_path)
                deleted_files.append(file_path)
        # 删除 __MACOSX 文件夹
        for d in dirs:
            if d == '__MACOSX':
                dir_path = os.path.join(root, d)
                os.rmdir(dir_path)
                deleted_files.append(dir_path)
    return deleted_files


def main():
    current_dir = os.getcwd()
    deleted_files = delete_macos_files(current_dir)

    if deleted_files:
        rst = "\n".join(deleted_files)
        message = f"Deleted the following files:\n{rst}"
    else:
        message = "No .DS_Store or __MACOSX files found."

    root = Tk()
    root.withdraw()
    messagebox.showinfo(f"Cleanup Result in {current_dir}", message)


if __name__ == "__main__":
    main()
