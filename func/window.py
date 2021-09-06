from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os

def chooseFile(mainwin:QWidget,title:str,fileTypes:list,allFiles:bool=False,cwd:str=os.getcwd())->tuple:
    '''
    弹出Qt文件选择对话框
    :param mainwin: 主窗口
    :param title: 窗口标题
    :param fileTypes: 可选择类型
    :param allFiles: 是否显示“所有文件”选项
    :param cwd: 起始位置
    :return: (
        选择成功，取消为False,
        文件路径
        文件类型
    )
    '''
    typeStr = ""
    for t in fileTypes[:-1]:
        typeStr += t + ';;'
    typeStr += fileTypes[-1]
    if allFiles:
        typeStr += ";;All Files (*.*)"
    fileName_choose, filetype = QFileDialog.getOpenFileName(mainwin,
                                                            title,
                                                            cwd,  # 起始路径
                                                            typeStr)  # 设置文件扩展名过滤,用双分号间隔

    if fileName_choose == "":
        return (False,"","")

    return (True,fileName_choose,filetype)

def warningBox(win,title,text):
    QMessageBox.warning(win,title,text)