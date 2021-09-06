import PyQt5.QtWidgets

from public import *
import re

from public import *
from func.data import *
import func.window as wf

import func.settingSave

#坐标输入规范
oldText = ["(,)","(,)","(,)"]

def changeCheck(id,tool:PyQt5.QtWidgets.QLineEdit):
        if re.search('^\([A-Z]*,[0-9]*\)$', tool.text()):
            oldText[id] = tool.text()
        elif re.search('^\([A-Z]*,[0-9]*\)$', tool.text().upper()):
            tool.setText(tool.text().upper())
            oldText[id] = tool.text().upper()
        elif tool.text() == "":
            tool.setText("(,)")
            oldText[id] = "(,)"
        else:
            tool.setText(oldText[id])
settingUi.le_idFirst.textChanged.connect(lambda: changeCheck(0,settingUi.le_idFirst))
settingUi.le_nameFirst.textChanged.connect(lambda: changeCheck(1,settingUi.le_nameFirst))
settingUi.le_pointsFirst.textChanged.connect(lambda: changeCheck(2,settingUi.le_pointsFirst))


#选择表格文件
def func_btnFindSheet():
    st,p,t = wf.chooseFile(mainwindow, '选择写入表格文件', ['Excel文件 (*.xls, *.xlsx)'], False)
    if st:
        sheetPath = p
        settingUi.le_sheetPath.setText(sheetPath)
        import func.sheetEdit as fs
        sheetList = fs.getFileSheet(sheetPath)
        settingUi.cb_chooseSheet.clear()
        for n in sheetList:
            settingUi.cb_chooseSheet.addItem(n)
    else:
        QMessageBox.information(settingwindow, "错误", "未选择表格文件")

settingUi.btn_findSheet.clicked.connect(func_btnFindSheet)


#设置按钮及返回按钮
def func_btnSetting():
    mainwindow.close()
    settingwindow.show()
    func.settingSave.loadSettingData()
mainUi.btn_setting.clicked.connect(func_btnSetting)

def func_btnBack(event):
    settingwindow.close()
    mainwindow.show()
    func.settingSave.saveSetting()
settingUi.btn_back.clicked.connect(func_btnBack)
settingwindow.closeEvent = (func_btnBack)