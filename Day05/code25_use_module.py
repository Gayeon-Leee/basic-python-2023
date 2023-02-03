# random 모듈 사용

import random

# print(random.choice(range(1, 7))) # => range 범위 안에서 무작위 출력
numbers = [i for i in range(1, 46)] # 1~45 리스트(배열)
lottery = []

for i in range(6):   # => 여기 있는 6은 0부터 시작하는 것임(0,1,2,3,4,5)
    lottery.append(random.choice(numbers))

print(lottery)