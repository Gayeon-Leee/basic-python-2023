# 모듈 사용
import math as m # => math 모듈 이름을 m 으로 명명해서 쓰겠다는 것 // 클래스로 안된 모듈
import code22_person as p # 우리가 만든 클래스
from code23_car import Car

print(m.pi)

print(m.tan(0))
print(m.ceil(3.8)) # ceil == 올림
print(2 ** 10)  # 정수
print(m.pow(2, 10))  # 실수 => 가급적이면 math 모듈에 있는게 정확해서 좋음


# 우리가 만든 모듈을 사용
me = p.Person('홍길순', 155, '여성')
print(me)

#
mycar = Car()
print(mycar)