import win32com.client
instCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
# print(instCpCybos.IsConnect)
if instCpCybos.IsConnect == 1:
    print("접속 정상")
else :
    exit()

instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")

#Set Input Value
#요청할 필드값
instMarketEye.SetInputValue(0,(4,67,70,111)) #현재가, PER, EPS, 최근분기년월
#조회할 종목에 대한 종목코드
instMarketEye.SetInputValue(1,('A035420','A035720'))#네이버

#요청
instMarketEye.BlockRequest()


print("현재가 : ", instMarketEye.GetDataValue(0,0))
print("PER : ", instMarketEye.GetDataValue(1,0))
print("EPS : ", instMarketEye.GetDataValue(2,0))
print("최근분기년월 : ", instMarketEye.GetDataValue(3,0))

print("")
print("현재가 : ", instMarketEye.GetDataValue(0,1))
print("PER : ", instMarketEye.GetDataValue(1,1))
print("EPS : ", instMarketEye.GetDataValue(2,1))
print("최근분기년월 : ", instMarketEye.GetDataValue(3,1))

