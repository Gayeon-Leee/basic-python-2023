# 예외처리
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

try: # => 수를 하나 또는 두개 초과 입력하는 단계에서 발생하는 예외 처리. 입력단계에서 적어주는 것
    x, y = input('두 수를 입력하세요 > ').split()
    x = int(x)
    y = int(y)
except Exception as e:
    print(e)
    exit() # => 필수. 안적으면 실행하면서 밑부분 예외처리랑 충돌해서 또 예외 발생할 수 있음
    #없으면 print(add(x, y)) 단계에서 name 'x' is not defined 예외메세지
finally:
    print('계속되나요?')    # 이거 실행 뒤 종료됨ㅋㅋ

# # 원시적인 예외처리
# if y == 0:  # 예외(zerodivision) 발생하지 않도록 하는것 => 다른거 처리에서 또 문제생김
#     print('y에 0을 넣지 마세요')
#     exit()



print('계산 테스트')

try:
    print(div(x, y))
# except ZeroDivisionError as e:
#     print('0으로 나누면 안돼요!')    #2. 이 부분 없어도 되는것! 코드가 복잡해지기만 한다. 사용자가 요청할 때만 만들면 됨~
except Exception as e:  # 여러개의 예외처리를 할 때 이 두 줄을 가장 마지막에 적어줘야함
    print(e)            # 마지막에 안적으면 다른 예외처리 실행 안됨
    # 1. 예외처리할때 이게 모든 예외를 다 잡아주기 때문에 그냥 이거 하나만 적어도 됨. 굳이 except 여러개 만들지 말것
finally: # 예외 발생 여부와 상관없이 수행
    print('계산은 계속됩니다!')

print(add(x, y))
print(mul(x, y))
