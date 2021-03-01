import win32com.client
instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

#set input value
instStockChart.SetInputValue(0, "A035420") #0 - 종목코드(네이버)
# 1- 요청구분(과거 데이터를 기간 or 개수로 조회)
instStockChart.SetInputValue(1, ord('2'))  #1 - 요청구분 (1 : 기간으로 요청, 2 : 개수로 요청)
# 4-요청 개수
instStockChart.SetInputValue(4, 60) # 6- 제일 최근 60개 일봉
# 5-요청할 데이터 종류
instStockChart.SetInputValue(5, 8) #8 - 거래량
# 6-요청할 차트의 종류
instStockChart.SetInputValue(6, ord('D')) # D - 일단위 데이터
# 9 - 수정주가 반영 여부
instStockChart.SetInputValue(9, ord('1')) #1 - 수정주가 반영

#요청
instStockChart.BlockRequest()

#Get data
volumes = []
numData = instStockChart.GetHeaderValue(3)

for i in range(numData):
    volume = instStockChart.GetDataValue(0,i)
    volumes.append(volume)

print(volumes)

avgVolume = (sum(volumes) - volumes[0])/(len(volumes)-1)

print(avgVolume)

if volumes[0] >= avgVolume*10:
    print("대박주")
else :
    print("일반 주 ",volumes[0]/avgVolume)




