import win32com.client
instCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
# print(instCpCybos.IsConnect)
if instCpCybos.IsConnect == 1:
    print("접속 정상")
else :
    exit()

instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
#
instStockChart.SetInputValue(0, "A035420") #0 - 종목코드(네이버)
# 1- 요청구분(과거 데이터를 기간 or 개수로 조회)
instStockChart.SetInputValue(1, ord('1'))  #1 - 요청구분 (1 : 기간으로 요청, 2 : 개수로 요청)
# 2-요청 종료일
instStockChart.SetInputValue(2, '20210201')  #1 - 요청구분 (1 : 기간으로 요청, 2 : 개수로 요청)
# 3-요청 시작일
instStockChart.SetInputValue(3, '20210101')  #1 - 요청구분 (1 : 기간으로 요청, 2 : 개수로 요청)
# 4-요청 개수
# instStockChart.SetInputValue(4, 10) #10 - 실제 요청할 데이터의 개수
# 5-요청할 데이터 종류
instStockChart.SetInputValue(5, (0,2,3,4,5,8)) #5 - 종가
# 6-요청할 차트의 종류
instStockChart.SetInputValue(6, ord('D')) # D - 일단위 데이터
# 9 - 수정주가 반영 여부
instStockChart.SetInputValue(9, ord('1')) #1 - 수정주가 반영

#요청
instStockChart.BlockRequest()

#응답 수신
numData = instStockChart.GetHeaderValue(3) # 수신한 데이터의 개수
numFiled = instStockChart.GetHeaderValue(1) # 수신된 데이터 내부의 필드 개수

print(str(numData) + " " + str(numFiled))



for i in range(numData):
    for j in range(numFiled):
        print(instStockChart.GetDataValue(j, i), end = " ")
    print("")
    # print(instStockChart.GetDataValue(j, i)) # j - 필드 , i - 데이터 수

