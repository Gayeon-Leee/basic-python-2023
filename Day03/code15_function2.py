# 함수

# 함수 만드는 방법 4가지
# 1. prameter(매개변수) O return O
# 2. prameter O return X
# 3. prameter x return O
# 4. prameter x return x

# 함수 정의
def add(x, y):      
    result = x + y  
    print(result)
    # return 

def sub(x, y):
    result = x - y
    print(result)
    # return

def mul(x, y):
    result = x * y
    print(result)
    # return

def div(x, y):
    result = x // y
    print(result)
    # return => return 없어도 v2의 값이 출력 => return 생략되어 있는 것임
    # 2. prameter O return X 의 경우임

def hello():
    print('Hello~!!!')
    return
# 3. prameter x return O 의 경우임

def hello2():
    msg = 'Hello, Hello'
    return  msg    
# 4. prameter x return x 의 경우임    
    
# 함수 호출
hello()
print(hello2())

# v1. 함수 정의에서 result 값을 출력 => return 할 값이 없기 때문에 None 으로 뜨는 것
val = add(1024, 5)
print(val)

val = sub(1024, 1000)
print(val)

val = mul(512, 2)
print(val)

val = div(108, 10)
print(val)

# v2. code14 파일과 같은 값으로 출력됨 => 함수 정의에 return이 생략되어 있는 것
add(1024, 5)    
sub(1024, 1000)
mul(512, 2)
div(108, 10)
