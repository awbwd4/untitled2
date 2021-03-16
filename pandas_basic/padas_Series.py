exam_dic = {'key1':'room1', 'key2':'room2'}
print(exam_dic['key1'])
print(exam_dic['key2'])

kakao_daily_closing_prices = [92600, 94400, 92100, 94300, 92300]

for price in kakao_daily_closing_prices:
    print(price)



kakao_daily_closing_prices2 = {
    '2021-03-02':92600
    ,'2021-03-03':94400
    ,'2021-03-04':92100
    ,'2021-03-05':94300
    ,'2021-03-06':92300
}

for price in kakao_daily_closing_prices2:
    print(price)

print(kakao_daily_closing_prices2['2021-03-02'])