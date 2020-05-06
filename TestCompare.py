import pytest as pytest

from Unittest.TianYanCha.Balance import xy, tyc

tycInterface = {'profit': 'balanceSheet',
                'balance': 'balanceSheet',
                'cashflow':'cashFlow'}


def transKeyFormat(key)->str:
    keylist =key.split('_')
    keys =keylist[0].lower()
    for k in range(1,keylist.__len__()):
        keys += keylist[k].capitalize()
    return keys

# 字段映射关系文件内容导入
def getTrans(fileName) -> dict:
    print('[open_file]:', fileName)
    f = open(fileName, 'r', encoding='utf-8')
    trans = {}
    for line in f.readlines():
        line = line.replace('\n', '')
        key = transKeyFormat(line.split(',')[0])
        value = line.split(',')[1]
        trans.update({key: value})
    return trans


def compare(interface, companyName, year, transFileName,col):
    # print('[][][][][][][][]',interface, companyName, year, transFileName)
    trans = getTrans(fileName=transFileName)
    xyData = xy(interface, companyName, year).getResult()['data']
    tycData = tyc(tycInterface[interface], companyName, year).getResult()['result'][col]

    for no in range(0, 4):
        print(xyData[no])
        print(tycData[no])
        for key in trans:
            # print(key)
            # print(trans[key])
            # print(xyData[no][key])
            # print(tycData[no][trans[key]])
            if tycData[no][trans[key]] != xyData[no][key]:
                print('[Question] [{}]:[{}] != [{}]:[{}]'.format(trans[key],tycData[no][trans[key]], key,  xyData[no][key]))
            # assert tycData[no][trans[key]] == xyData[no][key]
        print(f'============={no}==================')

# compare('profit', '厦门安妮股份有限公司', '2018', 'IncomeTrans','corpProfit')
# compare('balance', '厦门安妮股份有限公司', '2018', 'BalanceTrans','corpBalanceSheet')
compare('cashflow', '厦门安妮股份有限公司', '2018', 'CashTrans','corpCashFlow')
# compare('all', '厦门安妮股份有限公司', '2018', 'CashTrans','corpCashFlow')
