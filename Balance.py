import json
import requests

class xy:
    companyName = ''
    year = ''
    url = ''
    interface=''
    test = 'http://172.30.52.85:21108'

    def __init__(self, interface, companyName, year, host=test):
        self.url = f'{host}/spider-tax/finanical/{interface}?companyName={companyName}&year={year}'
        self.interface = interface
        print('[xy_url]',self.url)
        pass

    def getResult(self) -> dict:
        # print(self.url)
        result = requests.get(self.url)
        print('[xy]',result.text)
        f = open(self.interface+'_xy.json','w',encoding='utf-8')
        f.write(result.text)
        f.close()
        return json.loads(result.text)

class tyc:
    head = {"Authorization": "e617edb1-cddd-4fca-a334-272ba3d92271"}
    url=''
    interfaceTYC=''

    def __init__(self, interfaceTYC, companyName, year):
        self.url = f'http://open.api.tianyancha.com/services/open/stock/{interfaceTYC}/2.0?name={companyName}&year={year}'
        self.interfaceTYC=interfaceTYC
        print('[tyc_url]',self.url)
        pass

    def getResult(self)-> dict:
        result = requests.get(url=self.url, headers=self.head)
        print('[tyc]',result.text)
        f = open(self.interfaceTYC + '_tyc.json', 'w', encoding='utf-8')
        f.write(result.text)
        f.close()
        return json.loads(result.text)


# c = xy('all', '厦门安妮股份有限公司', '2018').getResult()
c = xy('cashflow', '厦门安妮股份有限公司', '2020').getResult()
# print(c)