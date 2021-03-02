#업종별 PER 분석

import win32com.client

instCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")

#업종별 코드 리스트(튜플 형태로 반환됨)
industryCodeList = instCpCodeMgr.GetIndustryList()

#업종별 코드로 업종명 구하기
for industryCode in industryCodeList :
    print(industryCode, instCpCodeMgr.GetIndustryName(industryCode))


print("\n\n\n\n\n\'")

# 식품업5를 가지고 해당 식품업에 속한 종목들 구하기
targetCodeList = instCpCodeMgr.GetGroupCodeList(5)
print(targetCodeList)

for targetCode in targetCodeList:
    print(targetCode, instCpCodeMgr.CodeToName(targetCode))

#식품업 종목들의 PER 평균
instMarketEye = win32com.client.Dispatch("CpSysDib.MarketEye")

instMarketEye.SetInputValue(0, 67)
instMarketEye.SetInputValue(1, targetCodeList)

instMarketEye.BlockRequest()

numStock = instMarketEye.GetHeaderValue(2) #2 - 종목 개수


sumPer = 0
for i in range(numStock):
    sumPer += instMarketEye.GetDataValue(0, i)

print("avg PER   ", sumPer/numStock)