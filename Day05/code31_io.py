# 입출력
# number = input('수를 입력하세요 > ')
# print(number * 5)   # 모든 입력값은 기본적으로 '문자'임 100을 입력하면 문자를 5번 곱하는것이기 때문에 100100100100100 이렇게 나옴

#수
number = int(input('수를 입력하세요 > ')) # => 입력값을 정수로 바꿔준 것
print(number * 5) # => 500 출력

#문자 
print('Life' 'is' 'short')
print('Life', 'is', 'short') # 공백을 주고싶으면 'Life ' 처럼 단어 뒤에 공백을 주거나 이렇게 쉼표 사용하면 됨

a = [1,2,3,4]
for i in a:
    print(i, end=' ')