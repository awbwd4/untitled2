import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")
codeList = instCpCodeMgr.GetStockListByMarket(1)

for i, code in enumerate(codeList):
   secondeCode = instCpCodeMgr.GetStockSectionKind(code)
   name = instCpCodeMgr.CodeToName(code)
   print(i, code, secondeCode, name)


