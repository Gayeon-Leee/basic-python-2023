# 좀 더 복잡한 계산기
def calc(option, *args):
    result = 0
    if option == 'add':
        for i in args:
            result += i

    elif option == 'mul':
        result = 1
        for i in args:
            result *= i

    elif option == 'sub':
        result = args[0]
        for i in args[1:]:
            result -= i

    elif option == 'div':
        result = args[0]
        for i in args[1:]:
            result /= i 

    return result        

print(calc('add', 5, 7, 17))        # 29                                 
print(calc('mal', 512, 2, 2))       # 2048                                
print(calc('sub', 10, 248, 396))    # -634
print(calc('div', 100, 5))          # 20.0
# 더하고 곱하는 등의 개수는 계속 추가할 수 있음

# 하나의 함수에 여러 값을 받을 수 있음 / 여러 값을 리턴할 때는 튜플을 사용
def calc(x,y):
    return (x*y, x/y)

res1, res2 = calc(5, 7)
print(res1, res2)

def new_calc(x,y):
    return (x*y, x/y, x+y, x-y)

res1, res2, res3, res4 = new_calc(5, 7)   
#받을 때는 튜플() 생략가능 => (res1, res2, res3, res4) = mul_and_div_and_add_and_sub(5, 7)
print(res1, res2, res3, res4)