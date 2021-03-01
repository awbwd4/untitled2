import win32com.client
instCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")

#정상 접속 여부 : 1이면 정상
print(instCpCybos.IsConnect)

#전체 종목 수
print('전체 종목 수 : '+str(instCpStockCode.GetCount()))

#각 인덱스에 해당하는 종목에 대한 데이터(0 - 종목코드, 1 - 종목명, 2 - FullCode)
print(instCpStockCode.GetData(1,0))

#각 인덱스에 해당하는 종목에 대한 데이터(0 - 종목코드, 1 - 종목명, 2 - FullCode)
print(instCpStockCode.GetData(0,0))

# 인덱스 첫번째~10번째 종목
for i in range(0, 10):
    print(instCpStockCode.GetData(1, i))

print(" ")

#NAVER 종목코드, 종목명 검색
stockNum = instCpStockCode.GetCount()

for i in range(stockNum):
    if instCpStockCode.GetData(1,i) == 'KAKAO':
        print(instCpStockCode.GetData(0,i))
        print(instCpStockCode.GetData(1,i))
        print(i)


print(" ")

naverCode = instCpStockCode.NameToCode('NAVER')
naverIndex = instCpStockCode.CodeToIndex(naverCode)
print(naverCode)
print(naverIndex)