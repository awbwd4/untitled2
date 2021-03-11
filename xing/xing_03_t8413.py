#차트 데이터 받아오기
#일봉 차트를 구성하는 일자, 시가, 고가, 저가, 종가 데이터 가져오기

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

class XAQueryEventHandlerT8413:
    query_state = 0

    def OnRecieveData(self, code):
        XAQueryEventHandlerT8413.query_state = 1


#------------------로그인-----------------------

id = input("웹 로그인 아이디: ")
passwd = input("웹 로그인 비밀번호: ")
cert_passwd = input("공인인증서 비번: ")


instXASession = win32com.client.DispatchWithEvents("XASession.XASession", XASessionEventHandler)
instXASession.ConnectServer("hts.ebestsec.co.kr", 20001)
instXASession.Login(id, passwd,cert_passwd, 0, 0)

while XASessionEventHandler.login_state == 0:
    pythoncom.PumpingWaitingMessage()


#-----------------T8413-----------------------

instXAQueryT8413 = win32com.client.DispatchWithEvents("XA_DataSet.XAQeury", XAQueryEventHandlerT8413)
instXAQueryT8413.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t8413.res"

instXAQueryT8413.SetFieldData("t8413InBlock", "shcode", 0, "078020")
instXAQueryT8413.SetFieldData("t8413InBlock", "gubun", 0, "2")
instXAQueryT8413.SetFieldData("t8413InBlock", "sdate", 0, "20210301")
instXAQueryT8413.SetFieldData("t8413InBlock", "edate", 0, "20210311")
instXAQueryT8413.SetFieldData("t8413InBlock", "comp_yn", 0, "N")


instXAQueryT8413.Request(0)

count_1 = 0
while XAQueryEventHandlerT8413.query_state == 0:
    pythoncom.PumpWaitingMessages()
    count_1 += 1
    if count_1 % 10000 == 0:
        print(count_1)
    if count_1 == 100000:
        count_1 = 0
        break

count_2 = instXAQueryT8413.GetBlockCount("t8413OutBlock1")
for i in range(count_2):
    date = instXAQueryT8413.GetFieldData("t8413OutBlock1","date",i)
    open = instXAQueryT8413.GetFieldData("t8413OutBlock1","open",i)
    high = instXAQueryT8413.GetFieldData("t8413OutBlock1","high",i)
    low = instXAQueryT8413.GetFieldData("t8413OutBlock1","low",i)
    close = instXAQueryT8413.GetFieldData("t8413OutBlock1","close",i)
    print(date, open, high, low, close)

