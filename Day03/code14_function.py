# 함수

# 함수 작동 순서
# 함수 정의 -> 정의만 한 것이지 실행이 아님
def add(x, y):      #def -> define으로 함수 정의한다는 것임
    result = x + y  # 3. add(1024, 5)이 여기로 올라와서 reult 값을 냄
    return result # 함수를 호출한 대상자에게 값을 돌려주는 것이 필요 => 4. result가 return을 만나면 호출한 val로 돌아감

# 함수 호출
val = add(1024, 5)  # 1. val 변수가  add 를 호출 => 2. add(1024, 5)를 들고 위로 올라감 
# 5. 함수를 호출한 val에 값을 돌려줌(return)
print(val)      # 6. val 값이 출력

# 함수 정의
def add(x, y):      
    result = x + y  
    return result

def sub(x, y):
    result = x - y
    return result

def mul(x, y):
    result = x * y
    return result

def div(x, y):
    result = x // y
    return result

# 함수 호출
val = add(1024, 5)
print(val)

val = sub(1024, 1000)
print(val)

val = mul(512, 2)
print(val)

val = div(108, 10)
print(val)

# 1. prameter O return O 의 경우임