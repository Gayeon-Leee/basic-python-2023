# 매개변수 개수 일정치 않은 경우
# def add(x, y, z, e, f ... ): 이런 식으로 매개변수가 늘어나는 등 개수 일정치 않은 것

def add(*args):
    result = 0
    for i in args:
        result += i
    
    return result    

print(add(1,2,3,4,5))
print(add(1,2,3,4,5,6,7,8,9,10))
print(add(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))
# 이런 식으로 개수가 몇개든 상관 없음