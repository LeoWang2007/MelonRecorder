from public import *
from func.data import *

#设置窗口功能
import settingAction

def submit_leStuname():
    #提交数据
    editTableByCommand(mainUi.le_stuname.text())
    mainUi.le_stuname.setText('')

mainUi.le_stuname.returnPressed.connect(submit_leStuname)