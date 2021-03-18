from pandas import Series, DataFrame

daeshin = {
    'open':[11650, 11100, 11200, 11300, 11400]
    ,'low':[12011, 11800, 11200, 11100, 11150]
    ,'high':[11160, 11050, 10900, 10950, 10900]
    ,'close':[11900, 11600, 11000, 11100, 10050, ]}


date = ['21.01.01','21.01.02','21.01.03','21.01.04','21.01.05']

daeshin_day = DataFrame(daeshin, columns=['open', 'low', 'high', 'close'], index=date)


print(daeshin)
print("=====================")
print(daeshin_day)

print("=====================")


#종가 데이터만 받아오기.
close = daeshin_day['close']
print(close)


# close2 = daeshin_day['21.01.01']\

# print(close2)


# dataframe 객체의 로우값에 접근하려면 .ix 메서드를 사용해야함.
# ix 메서든 ->현재는 사라진 메서드임.
# 레이블과 위치 정수 둘 다 사용가능하다는 장점 -> 인덱싱 할 시 모호해짐.

# day_data = daeshin_day.ix['21.01.01']
day_data = daeshin_day.loc['21.01.01']
print(day_data)
print(type(day_data))

print(daeshin_day.columns)
print(daeshin_day.index)
