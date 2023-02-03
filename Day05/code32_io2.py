# 다중입력
# x, y = input('두 영단어를 입력하세요 > ').split()

# print(x)
# print(y)

# 완전 다중입력(개수 몇개든지 상관없음)
inputs = list(map(str, input('단어를 입력하세요(개수상관없음) > ').split())) # map 은 들어오는 값들을 나열해주는 것
# str 에는 숫자 입력할 수 있음 => 수도 문자로 받을 수 있기 때문
print(inputs)

inputs = list(map(int, input('정수를 입력하세요(개수상관없음) > ').split()))
# int에는 문자 입력 불가 => error 남
print(inputs)