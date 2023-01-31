# 자료형
# None : 값이 없는 값
None

print(None)
print(0 == None)
print('' == None)  # None 도 하나의 값으로 보기 때문에 0, '' 과 같냐고 하면 false 뜨는 것

# 숫자형
val = 3
print(type(val)) 

val = 3.14
print(type(val)) 

val = 'Hello'
print(type(val))  #같은 val 이라도 어떤 값을 넣는지에 따라 바로 class 값 바뀜

val = 0b1010
print(type(val))  #2진수도 int 로 나옴

val = 21.213734893749832789
print(type(val))    # 이런 큰 값도 float

val = 4_520_000     # 보통 통화단위에서 ,로 1000단위 구분하는 것 처럼 읽기 편하게 _ 사용 가능
print(val)          # 출력값은 그냥 4520000 나옴

val = 3_099.99
print(val)

#문자열
val = 'Life is short, You need Python.'
print(val)
print(type(val))

val = 'Hello\nWorld!'   #탈출문자 \n 한줄 내리기
print(val)
val = 'Hello\tWorld'    #\t 스페이스4번
print(val)
val = 'Hello\t\bWorld'  #\b 백스페이스
print(val)

val = '''Life is short,
you need Python.'''     # ''' 없이 사용하면 오류. ''' 넣어서 줄 구분 가능
print(val)
val = "Hi, I'm 'Gayeon'"   
print(val)
val = 'Hi, I\'m \'Gayeon\''     
print(val)  # 쌍따옴표 홑따옴표 구분없이 동일하지만 홑따옴표를 문장 안에 부호로 사용할 경우에는 쌍따옴표 사용이 편함

# 불린형(Boolean) 또는 불형
참 = True
거짓 = False
print(type(거짓))   #class 'bool' 

print(1 + 1 == 2)
# 거짓이라는 False 값 변수가 참이냐
print(거짓 == True)
print(거짓 == False)
print(거짓 is False)

print(bool(1)) # 1 == True
print(bool(0)) # 0 == False
print(bool(2)) # 1 이상의 값은 True 로 용인해주지만 다른 언어에서는 0,1 만 취급하니 0,1 만 사용