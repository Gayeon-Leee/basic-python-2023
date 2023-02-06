# Car 클래스를 상속한 제네시스 클래스
# 부모의 class 를 그대로 사용할 수 있고, 새로운 내용을 추가할 수 있으며, 부모 클래스의 내용을 재정의해서 쓸 수 있음

from code38_car import Car

# child class
class Genesis(Car):
    def __init__(self, name, color, 
                 plate_number, product_year) -> None:
        super().__init__() # 부모클래스 초기화 하라는 것

        self.__name = name
        self.__color = color
        self.__plate_number = plate_number
        self.__product_year = product_year
        print(f'{self.__name} 인스턴스 생성!')
    
    def set_name(self, name): # 부모 클래스에 없는 정의 추가할 수 있음
        self.__name = name

    def get_name(self): # 이렇게 이름을 재정의 해주지 않으면 33열에서 계속 부모의 이름을 사용함
        return self.__name

    def run(self):  # 부모 클래스의 run이랑 다르게 재정의 해준 것
        return f'{self.__name}이(가) 달립니다.'
    
    # def stop(self): # 이 부분 주석 해제하면 stop 부분도 팔공이로 출력
    #     return f'{self.__name}이(가) 멈춥니다.'
    

gv80 = Genesis('팔공이', 'black', '66오 1004', 2022)
#gv80.set_name('팔공이') 위에 초기화 안했을때 이름 지어줄 수 있는 방법,,

print(f'이 차의 이름은 {gv80.get_name()} 입니다.') 
print(gv80.run()) # 부모의 run을 재정의했기 때문에 팔공이가 달린다고 출력됨
print(gv80.stop()) # 부모의 stop 재정의 부분이 주석처리 되어있어 차가 멈춘다고 출력됨~