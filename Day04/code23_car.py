import os
import code


# 자동차 클래스
class Car:
    __number = '54라 9538'

    def get_number(self):
        return self.__number
    
    # 클래스 외부에선 변경X, 멤버함수로는 내부를 조작 가능
    def __init__(self, number='54라 9538') -> None:
        self.__number = number # => __number로 원래 값 변경 못하게 한 것 이렇게 해서 바꿔출력하게 해줌
        print('__init__')
        
    # def __new__(cls):
    #     print('__new__')
    #     return super().__new__(cls) # super => 부모클래스
    
    def __str__(self) -> str:
        return f'차 번호는 {self.__number}'
    
yourcar = Car(number='88호 7486') 
print(yourcar)
yourcar.__number = '54라 9999' # => 외부에서는 멤버변수에 접근불가 (값이 안바뀜)
print(yourcar)  
print('클래스 내부함수 사용!')
yourcar.set_number('55오 5555')
print(yourcar)

mycar = Car()
print(mycar)
print(f'제 차는 아이오닉이고, 번호가 {mycar.get_number()}에요.')

mycar.__number = '132거 8874'  # => number 에 __ 없으면 여기서 '132거 8874'로 출력되어야함. __ 붙여서 값 바꿀 수 없게 하는 것
print(mycar)

