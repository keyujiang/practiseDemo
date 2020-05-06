import requests


class income:
    companyName = '上海新颜人工智能科技有限公司'
    year = '2019'
    url = f'http://172.30.38.16:21108/spider-tax/finanical/profit?companyName={companyName}&year={year}'

    def __init__(self, companyName, year):
        self.url = f'http://172.30.38.16:21108/spider-tax/finanical/profit?companyName={companyName}&year={year}'
        # print(self.companyName,self.year)
        pass

    def getResult(self):
        print(self.url)
        result = requests.get(self.url)
        print(result.text)
        return result.text

c = income('厦门安妮股份有限公司','2018')
c.getResult()