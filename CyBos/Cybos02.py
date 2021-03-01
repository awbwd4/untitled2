import win32com.client


instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")

# GetStockListByMarket 시장구분에 따라 주식 종목을 리스트 형식으로 제공, 1 - 튜플형식으로 반환
codeList = instCpCodeMgr.GetStockListByMarket(1)

# print(codeList)

kospi = {}
for code in codeList:
    name = instCpCodeMgr.CodeToName(code)
    kospi[code] = name

# print(kospi)

#엑셀로 저장
f = open('C:\\Users\\JaeukKo\\Desktop\\trading_algorithm\\kospi.csv', 'w')

for key, value in kospi.items():
    f.write("%s,%s\n"%(key,value))

f.close()

