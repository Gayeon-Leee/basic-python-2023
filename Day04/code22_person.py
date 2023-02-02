# 클래스 생성
class Person: # 여기서 person은 class를 만든 것
    name = '익명'       ##명사 == 변수
    height = ''
    gender = ''
    blood_type = 'A'

    # 1. 생성자 추가
    # def __init__(self): #-> None: # -> None은 return 값이 없을때 사용, 생략가능
    #     self.name = 'ron'
    #     self.height = '175'
    #     self.gender = 'male'
    #     self.blood_type = 'B'

    # def __init__(self, name, height, gender)-> None:
    #     self.name = name
    #     self.height = height
    #     self.gender = gender

    def __init__(self, name = 'ron', height = '175', gender = 'male')-> None:
        self.name = name
        self.height = height
        self.gender = gender    

    def walk(self):         ##동사 == 함수
        print(f'{self.name}이(가) 걷습니다.')

    def run(self, option):    ##함수의 parameter == option
        if option == 'Fast':
            self.walk() # => run 하기 전에 walk 함수를 먼저 실행할 수도 있음
            print(f'{self.name}이(가)빨리 뜁니다')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다')

    def stop(self):     # class 안에 들어가는 함수는 무조건 self parameter가 들어가야함
        print(f'{self.name}이(가) 멈춥니다.')   
# 흰색 실선으로 함수나 제어문의 해당구간을 볼 수 있음

# 2. 생성자 외 매직매서드(펑션) __str__
def __str__(self)-> str:
     return f'출력! 이름은 {self.name}, 성별은 {self.gender}'

harry = Person('potter', 170, 'male') # person() class를 만들어서 객체(실체)를 만들라는 뜻  
                 # 위의 person 이라는 class를 가지고 harry 라는 객체를 만든 것 => 이렇게 만들어진 객체를 instance 라고 함
harry.name = 'potter'   # harry 라는 객체에 name 이라는 변수를 부여 => name 이라는 개별 변수에서 객체와 만나 구조화 된 것
harry.height = '170'
harry.gender = 'male'
harry.blood_type = 'A'

print(f'{harry.name}의 혈액형은 {harry.blood_type}입니다.')

harry.run('Fast')
print(harry) # 여기서 출력되는건 메모리 주소

# 1. 초기화 후 객체생성
ron = Person('론', 175, 'male')
ron.run('Slow') # 생성자에서 초기화를 했기 때문에 name 지정을 안해도 되는것
# 이상태에서 harry.name~ 을 주석처리하면 다 ron 으로 출력
print(ron) # 여기서 출력되는건 메모리 주소

print('==============================')
# 2. parameter를 받는 생성자 실행
hermione = Person('헤르미온느', 165, 'female')
print(hermione.name)
print(hermione.height)
print(hermione.gender)
print(hermione)