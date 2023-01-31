# 복합형

#리스트를 안쓰면
a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5
a6 = 6
a7 = 7
a8 = 8
a9 = 9
a10 = 10

print(a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10)
print(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)

# 리스트 = 배열..리스트 쓰면 위의 내용을 훨씬 간단하게 작성할 수 있음
arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)
sum = 0
for i in arr:
    sum += i

print(sum)    

arr1 = [1,2,3]
arr2 = [1.1,2.2,3.3]
arr3 = ['Hello', 13, 'World!', True]
print(arr3)    
print(type(arr3))   #class 'list'
print('arr1의 2번 인덱스값' + str(arr[2]))

arr4 = [] # 빈 리스트
arr5 = list()
print(arr5)

arr6 = [1,2,3,4,[5,6,7,8,[9,10]]]
print(arr6)

arr7 = [[1,2,3,4],[5,6,7,8]]    #arr6,7 같이 list 안에 list 가능.. 
print(arr7)

# 튜플
tuple1 = (1,2,3,4)
print(tuple1)

arr5.append(4)    #비어있던 list 에 값 넣어준 것
print(arr5)

# tuple1.append(4)    #tuple = 배열 // list와 다르게 한번 만들면 값 변경 불가
# print(tuple1)       #값 변경 불가능한데 지정하여 이대로 프린트 실행하면 오류 발생하여 주석처리함
print(type(tuple1))

# 딕셔너리 (Dictionary)
theboywholived = {'name' : 'Harry Potter', 
                  'age' : 11, 
                  'dormitory' : 'Gryffindor',
                  'friends' : 'Ron, Hermione'}   # 가로로 길게 늘여 쓰기 보다는 이렇게 한 눈에 보이게 쓰는게 좋음

print(theboywholived)
print(theboywholived['dormitory'])    # 키(dormitory)에 대한 값(gryffindor) 출력되는 것 / ctrl + space 알아두기
print(theboywholived['friends'])
print(type(theboywholived))           # class 'dict'

# 집합
set1 = set([1,2,3,4])
print(set1)

set1 = set("Hello World")   
print(set1)     # 분리되어 출력됨