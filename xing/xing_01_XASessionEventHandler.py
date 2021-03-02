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

instXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEventHandler)

id = input('웹 로그인 아이디 : ')
pwd = input('웹 로그인 암호 : ')
cert_pwd = input('공인인증서 암호 : ')

# instXASession.ConnectServer("hts.ebest.co.kr", 20001)
# instXASession.ConnectServer("demo.ebest.co.kr", 20001)
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