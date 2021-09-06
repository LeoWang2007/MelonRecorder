from PyQt5.QtWidgets import *
import PyQt5.QtCore as QtCore
from PyQt5.QtGui import *

import sys
import os
from threading import Thread

#主窗口及Qt应用
import mainwin
import settingwin#界面

sheetPath = ""

app = QApplication(sys.argv)
#app.setStyle("macintosh")
mainwindow = QWidget()
mainUi = mainwin.Ui_Form()
mainUi.setupUi(mainwindow)
mainwindow.setFixedSize(mainwindow.width(),mainwindow.height())
settingwindow = QWidget()
settingUi = settingwin.Ui_Form()
settingUi.setupUi(settingwindow)
settingwindow.setFixedSize(settingwindow.width(),settingwindow.height())
mainwindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
settingwindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
# mainwindow.setWindowFlags(Qt.WindowStaysOnBottomHint)