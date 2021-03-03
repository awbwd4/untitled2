import win32com.client
import pythoncom

#콜백 메서드
class XASessionEventHandler:
    login_state = 0

    def OnLogin(self, code, msg):
        if code == "0000":
            print('로그인 성공')
            XASessionEventHandler.login_state = 1
        else:
            print('로그인 실패')


class XAQueryEventHandlerT1102:
    query_state = 0

    def OnRecieveDate(self, code):
        XAQueryEventHandlerT1102.query_state = 1


##로그인

instXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEventHandler)

id = input('웹 로그인 아이디 : ')
pwd = input('웹 로그인 암호 : ')
cert_pwd = input('공인인증서 암호 : ')

# instXASession.ConnectServer("hts.ebest.co.kr", 20001)
# instXASession.ConnectServer("demo.ebest.co.kr", 20001) #모의 투자
instXASession.ConnectServer("hts.ebestsec.co.kr", 20001)
instXASession.Login(id,pwd,cert_pwd,0,0)

#접속될때까지 콜백 반복
while XASessionEventHandler.login_state == 0:
    pythoncom.PumpWaitingMessages()

#계좌 조회
num_account = instXASession.GetAccountListCount()
print('총 보유 계좌 수 : ', num_account)

for i in range(num_account):
    account = instXASession.GetAccountList(i)
    print('계좌번호 : ', account)






instXAQueryT1102 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandlerT1102)

# C
instXAQueryT1102.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t1102.res"


instXAQueryT1102.SetFieldData("t1102InBlock","shcode",0,"078020") #블록명, 필드명, 0-단일데이터, 필드입력값

instXAQueryT1102.Request(0)

count = 0

while XAQueryEventHandlerT1102.query_state == 0:
    pythoncom.PumpWaitingMessages()
    count += 1
    if count % 10000 == 0:
        print(count)
    if count == 100000:
        break


name = instXAQueryT1102.GetFieldData("t1102OutBlock","hname",0)
price = instXAQueryT1102.GetFieldData("t1102OutBlock","price",0)

print(name)
print(price)