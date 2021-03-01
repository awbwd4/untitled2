import win32com.client

class CpStockCode:
    def __init__(self):
        self.stocks = {'유한양행':'A000100'}

    def GetCount(self): # 주식 종목 수 리턴
        return len(self.stocks)

    def NameToCode(self, name): #종목명을 입력하면 해당 종목의 코드를 리턴
        return self.stocks[name]

instCpStockCode = CpStockCode()

cnt = instCpStockCode.GetCount()

code = instCpStockCode.NameToCode('유한양행')



explore = win32com.client.Dispatch("InternetExplorer.Application")

word = win32com.client.Dispatch("Word.Application")

explore.Visible = True
word.Visible = True