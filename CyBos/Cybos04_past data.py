import win32com.client
instCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
print(instCpCybos.IsConnect)
instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
#
# instStockChart.SetInputValue(0, "A003540") #0 - 종목코드
# 1- 요청구분(과거 데이터를 기간 or 개수로 조회)
instStockChart.SetInputValue(1, ord('2'))  #1 - 요청구분 (1 : 기간으로 요청, 2 : 개수로 요청)
# 4-요청 개수
instStockChart.SetInputValue(4, 20) #10 - 실제 요청할 데이터의 개수
# 5-요청할 데이터 종류
instStockChart.SetInputValue(5, 5) #5 - 종가
# 6-요청할 차트의 종류
instStockChart.SetInputValue(6, ord('D')) # D - 일단위 데이터
# 9 - 수정주가 반영 여부
instStockChart.SetInputValue(9, ord('1')) #1 - 수정주가 반영

#요청
instStockChart.BlockRequest

#응답 수신
numData = instStockChart.GetHeaderValue(3)
for i in range(numData):
    print(instStockChart.GetDataValue(0, i))
