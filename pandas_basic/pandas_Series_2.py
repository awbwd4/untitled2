from pandas import Series, DataFrame

kakao = Series([92600, 92400, 92100, 94300, 92300])
print(kakao)

for i in range(4):
    print(kakao[i])


kakao2 = Series([92600, 92400, 92100, 94300, 92300], index=['20210301', '20210302','20210303','20210304','20210305'])


print(kakao2)

print(kakao2['20210301'])

for date in kakao2.index:
    print(date)



for closing_price in kakao2.values:
    print(closing_price)




mine = Series([10,20,30], index=['naver','sk','kt'])
friend = Series([10,30,20], index=['kt','naver','sk'])


merge = mine+friend
print(merge)