import requests

class income971:
    companyName = '上海新颜人工智能科技有限公司'
    year = '2019'
    id='7996092'
    url = f'http://open.api.tianyancha.com/services/open/stock/profit/2.0?id={id}&companyName={companyName}&year={year}'
    head ={"Authorization":"e617edb1-cddd-4fca-a334-272ba3d92271"}

    def __init__(self, companyName, year):
        self.url = f'http://open.api.tianyancha.com/services/open/stock/profit/2.0?companyName={companyName}&year={year}'
        pass

    def getResult(self):
        result = requests.get(url=self.url, headers=self.head)
        print(result.text)
        return result.text


c=income971('厦门安妮股份有限公司','2018')
c.getResult()