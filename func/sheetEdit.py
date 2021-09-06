import openpyxl as ox

def getFileSheet(path):
    f = ox.load_workbook(path)
    s = f.sheetnames
    f.close()
    return s