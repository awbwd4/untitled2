from pandas import DataFrame

#딕셔너리 생성
raw_data = {
     'col0':[1,2,3,4]
    ,'col1':[10,20,30,40]
    ,'col2':[100,200,300,400]
}

#col0, col1, col2 -> dataframe의 각 칼럼을 인덱싱함.
#로우 방향으로는 Series와 유사하게 정숫값으로 자동으로 인덱싱됨.


#생성된 딕셔너리를 dataframe 생성자로 넘겨주면
#dataframe 객체가 생성됨
data = DataFrame(raw_data)

print(data)