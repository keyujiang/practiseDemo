import json

def transKeyFormat(key)->str:
    keylist =key.split('_')
    keys =keylist[0].lower()
    for k in range(1,keylist.__len__()):
        keys += keylist[k].capitalize()
    return keys

# 映射关系
f = open('BalanceTrans', 'r', encoding='utf-8')
trans={}
for line in f.readlines():
    line=line.replace('\n','')
    key= transKeyFormat(line.split(',')[0])
    value =line.split(',')[1]
    trans.update({key:value})
print('[trans]',trans)

# 载入xy数据
f = open('Balance.json', 'r', encoding='utf-8')
income=json.load(f)['data']

# 载入tyc数据
f = open('Balance972.json', 'r', encoding='utf-8')
income971=json.load(f)['result']['corpBalanceSheet']

for no in range(0,4):
    # print(income[no])
    # print(income971[no])
    for key in trans:
        # print(key)
        # print(trans[key])
        # print(income[no][key])
        # print(income971[no][trans[key]])
        if income971[no][trans[key]] != income[no][key]:
            print(trans[key],key,income971[no][trans[key]],income[no][key])
    print(f'===============[{no}]===================')
