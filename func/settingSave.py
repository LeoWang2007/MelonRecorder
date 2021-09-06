from public import *
import json
import func.sheetEdit
import os

def saveSetting():
    settingData = {}
    settingData['path'] = settingUi.le_sheetPath.text()
    settingData['sheet'] = settingUi.cb_chooseSheet.currentText()
    settingData['idF'] = settingUi.le_idFirst.text()
    settingData['nameF'] = settingUi.le_nameFirst.text()
    settingData['pointF'] = settingUi.le_pointsFirst.text()
    with open('data/setting.wmc','w+') as f:
        f.write(json.dumps(settingData))

def loadSettingData():
    with open('data/setting.wmc', 'r') as f:
        settingData:dict = json.loads(f.read())
    settingUi.le_sheetPath.setText(settingData.get('path','未找到文件参数'))
    if os.path.exists(settingData.get('path')):
        sheetList = func.sheetEdit.getFileSheet(settingData.get('path'))
        settingUi.cb_chooseSheet.clear()
        for n in sheetList:
            settingUi.cb_chooseSheet.addItem(n)
    else:
        settingUi.le_sheetPath.setText('文件不存在')
    settingUi.cb_chooseSheet.setCurrentText(settingData.get('sheet'))
    settingUi.le_idFirst.setText(settingData.get('idF'))
    settingUi.le_nameFirst.setText(settingData.get('nameF'))
    settingUi.le_pointsFirst.setText(settingData.get('pointF'))