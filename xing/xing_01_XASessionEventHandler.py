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


class XAQueryEventHandlerT8430:
    query_state = 0

    def OnRecieveDate(self, code):
        XAQueryEventHandlerT8430.query_state = 1


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

# xingAPI는 각 요청 작업을 구분하기 위해 TR코드를 사용
# 해당 TR코드에 대한 res 파일을 인스턴스에 등록하여
# 서버가 어떤 TR 요청을 받은 것인지를 구분할 수 있게 함.
instXAQueryT1102.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t1102.res"


instXAQueryT1102.SetFieldData("t1102InBlock","shcode",0,"078020") #블록명, 필드명, 0-단일데이터 조회시, 필드입력값

#입력 데이터를 서버로 전송
instXAQueryT1102.Request(0)

count = 0

# 서버에 TR요청을 했다면 해당 작업이 완료됐다는 이벤트를 받을 때 까지
# 프로그램이 종료하지 않고 대기.
while XAQueryEventHandlerT1102.query_state == 0:
    # TR 처리가 완료되면 OnRecieveData를 콜백, queru_state 값이 1로 변경.
    pythoncom.PumpWaitingMessages()
    count += 1
    if count % 10000 == 0:
        print(count)
    if count == 100000:
        count = 0
        break


name = instXAQueryT1102.GetFieldData("t1102OutBlock","hname",0)
price = instXAQueryT1102.GetFieldData("t1102OutBlock","price",0)

print(name)
print(price)


# 반복 데이터 조회. t8430 : 주식종목조회

#res 파일 등록
print("=========1====================")
instXAQueryT8430 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandlerT1102)
print("=========2====================")
instXAQueryT1102.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t8430.res"

# 요청 필드값 세팅 - 유가증권시장(코스피) 주식 종목 조회
print("=========3====================")
instXAQueryT8430.SetFieldData("t8430InBlock","gubun",0,1) #단일 데이터 조회, 1- 유가증권(코스피)

# 요청
print("=========4====================")
instXAQueryT8430.Request(0)


#콜백이 올 때 까지 대기
print("=========5====================")
while XAQueryEventHandlerT8430.query_state == 0:
    pythoncom.PumpWaitingMessages()
    count += 1
    if count % 10000 == 0:
        print(count)
    if count == 100000:
        count = 0
        break


#데이터의 총 개수.
count = instXAQueryT8430.GetBlockCount("t8430OutBlock")
print("주식종목조회 데이터의 총 개수 : ", int(count))


for i in range(5):
    hname    = instXAQueryT8430.GetFieldData("t8430OutBlock","hname",i)
    shname   = instXAQueryT8430.GetFieldData("t8430OutBlock","shname",i)
    expcode  = instXAQueryT8430.GetFieldData("t8430OutBlock","expcode",i)
    etfgubun = instXAQueryT8430.GetFieldData("t8430OutBlock","etfgubun",i)
    print(i, hname, shname, expcode, etfgubun)