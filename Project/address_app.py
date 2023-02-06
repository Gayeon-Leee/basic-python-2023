# 주소록앱 _ 사용자가 정보 입력
# 2023-02-06
# Yeon
# 24. 예외처리
# 24-1 파일 없을때 나는 예외
# 24-2 입력시 / 개수가 다를 때 예외
# 24-3 메뉴변호 입력 숫자외 예외

import os # 화면 클리어 기능 만들려고 운영체제용 os 불러오는 것

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
    
    # 13. 객체 존재 여부 확인 => 삭제 하기 위함
    def isNameExist(self, name):
        if self.__name == name:
            return True
        else:
            return False
        
    # 18. 각 멤버변수에 접근하는 함수
    # getName, getPhoneNum, getEmail, getAddr
    def getName(self) -> str:
        return self.__name
    
    def getPhoneNum(self) -> str:
        return self.__phone_num
    
    def getEmail(self):
        return self.__email
    
    def getAddr(self):
        return self.__addr

# 만든순서 5 사용자가 입력하도록
def set_contact():
    name, phon_num, email, addr = input('정보입력(이름/전번/이메일/주소)' ).split('/') # split 하기 위해 , 말고 구분자 / 사용한 것
    # 만든순서 7. contact 객체 만들기
    contact = Contact(name, phon_num, email, addr) #email=email, addr=addr 이런식으로 하면 순서 바꿔서 넣을 수 있지만 잘 쓰지X
    return contact

# 만든순서 11 주소록 출력
def get_contacts(list):
    for item in list:
        print(item)
        print('===================')

#14. 주소록 삭제
def del_contact(list, name):
    count = 0 # 16 찾는 이름 카운트
    for i, item in enumerate(list): # 리스트 인덱스 추가생성
        if item.isNameExist(name):
            count += 1 # 1 증가
            del list[i] # 리스트에서 i번째 데이터를 삭제하겠다는 것

    if count > 0: # 17 메세지 출력
        print('삭제했습니다.')
    else:
        print('삭제할 주소록이 없습니다.')        

# 19. 주소록 파일 저장
def save_contacts(list):
    file = open('C:/Source/studyPython2023/Project/contacts.txt','w',
                encoding='utf-8') # 파일 생성할 절대경로 복붙 후 역슬래시 -> 슬래시로 바꾸고 타입입력, 인코딩
    for item in list:
        text = f'{item.getName()}/{item.getPhoneNum()}/{item.getEmail()}/{item.getAddr()}'
        file.write(f'{text}\n')

    file.close() # 파일은 마지막에 꼭 닫아줘야함

#21. 주소록 읽어오기
def load_contacts(list):
    try:
        file = open('C:/Source/studyPython2023/Project/contacts.txt','r',
                encoding='utf-8')   # 읽어오는거라 타입 r
    except Exception as e: # 24-1 파일 없을때 나는 예외 => 이렇게하면 파일 생성하고 
        f = open('C:/Source/studyPython2023/Project/contacts.txt','w',
                encoding='utf-8')
        f.close() # 24-1 이렇게하면 파일 생성하고 함수에서 나감
        return
        
    while True:
        line = file.readline().replace('\n','') # 23. 문장끝 \n 제거
        if not line: break

        lines = line.split('/')
        contact = Contact(lines[0], lines[1], lines[2], lines[3])
        list.append(contact)

    file.close()     

# 만든순서 8. 추가. 화면 클리어
def clear_console():
    command = 'clear' # Linux, Unix 화면 클리어 명령어
    if os.name in ('nt', 'dos'): # 'nt', 'dos' == Window 운영체제라면
        command = 'cls' # 윈도우 화면 클리어 명령어

    os.system(command)    

# 만든순서 6
def get_menu():
    str_menu = ('주소록앱 v1.0\n'
                '1. 연락처 추가\n'
                '2. 연락처 출력\n'
                '3. 연락처 삭제\n'
                '4. 앱 종료')
    print(str_menu) 
    try:  #24-3 메뉴변호 입력 숫자 외 예외처리 
        menu = int(input('메뉴입력 : '))
    except Exception as e:
        menu = 0 #24-3 메뉴번호에 영문자나 특수문자 넣으면 전부 0으로 => 예외발생 안하고 그냥 입력값 무시
    return menu


# 만든순서 3 전체 실행
def run(): # => 클래스 내의 함수 아니라 self 안씀
    contacts = list() # 10. 주소를 담기 위한 빈 리스트 생성
    load_contacts(contacts) # 22. 주소록 읽어오기
    # temp = Contact('이가연', '010-2430-5102', 'gy9411@naver.com',
    #                '부산 부산진구') # 줄바꿈할때 , 안찍어서 오류났었음! 인자 사이에 , 중요
    # set_contact()
    clear_console() # 부가적인 명령
    while True:
        sel_menu = get_menu()
        if sel_menu == 1: # 9. 연락처 추가
            try: # 24-2 입력시 / 개수가 다를 때 예외
                contact = set_contact()
                contacts.append(contact)
                input('주소록 입력 성공') 
            except Exception as e:
                print('이름/전번/이메일/주소순으로 똑바로 입력하세요')
                input() # 13. 아무것도 안받는 입력이었는데 예외처리 하느라 try 안으로 들어감
            finally:    
                clear_console()             
        elif sel_menu == 2: #12. 연락처 출력
            get_contacts(contacts)
            input('주소록 출력 완료')
            clear_console()
        elif sel_menu == 3: #15 연락처삭제
            name = input('삭제할 이름 입력 : ')
            del_contact(contacts, name)
            input()
            clear_console()
        elif sel_menu == 4: # 20 앱종료시 주소록 파일에 저장
            save_contacts(contacts)
            break
        else:
            clear_console()

# 만든순서 1 메인실행영역
if __name__ == '__main__':
    # print('주소록앱 시작합니다.')
    run() # 전체 디버깅할때 여기에 중단점 찍어야함. 천천히 한 번 해볼 것!!