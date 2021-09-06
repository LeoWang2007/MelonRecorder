from public import *

def splitCommandString(s:str):
    while s[-1:] == ' ':#保证末尾没有空格
        s = s[:-1]
    pair = False#是否为双数据传参
    try:
        a,b = s.split(' ')
        pair = True
        return (pair, (a, b))
    except:
        a = s
        pair = False
        return (pair, a)

def handleScoreString(s:str):
    '''
    处理分数字符串
    +开头为正数
    -或‘’开头为负数
    :param s: 待处理数字 str
    :return: 处理完成数字 int
    '''
    try:
        num = int(s)
    except:
        return None
    if s[0] == '+':
        return num
    else:
        return -abs(num)

def editTableByCommand(command):
    pair,cmd = splitCommandString(command)
    if pair:
        stu,edit = cmd
        edit = handleScoreString(edit)
    else:
        stu = cmd
        edit = -1
    if edit == None:
        return
    print(stu)
    print(edit)
