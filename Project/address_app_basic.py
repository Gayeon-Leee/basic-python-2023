# 주소록앱 _ 입력 되어있던 값만 출력
# 2023-02-06
# Yeon

#만든순서 2 클래스 생성
class Contact:
    # 생성자 - 이름, 전번, 이메일, 주소 => 여러 parameter 받을거라 생성자 필요한 것
    def __init__(self, name, phone_num, email, addr) -> None:
        self.__name = name
        self.__phone_num = phone_num
        self.__email = email
        self.__addr = addr

    # 만든순서 4 __str__ 재정의
    def __str__(self) -> str:
        str_res = (f'이  름 : {self.__name}\n' 
                   f'핸드폰 : {self.__phone_num}\n'
                   f'이메일 : {self.__email}\n'
                   f'주  소 : {self.__addr}')  # 여러 줄 쓰려면 () 써서 묶어줘야함
        return str_res


# 만든순서 3 전체 실행
def run(): # => 클래스 내의 함수 아니라 self 안씀
    temp = Contact('이가연', '010-2430-5102', 'gy9411@naver.com',
                   '부산 부산진구') # 줄바꿈할때 , 안찍어서 오류났었음! 인자 사이에 , 중요
    print(temp)

# 만든순서 1 메인실행영역
if __name__ == '__main__':
    print('주소록앱 시작합니다.')
    run()