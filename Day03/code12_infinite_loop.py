# 무한반복 예제
num = 0

while True:
    print('메뉴를 선택하세요.')
    print('  1. 회원입력')
    print('  2. 회원검색')
    print('  3. 회원수정')
    print('  4. 회원삭제')
    print('  5. 프로그램 종료')
    num = input('메뉴번호 입력 > ') # '1' => 입력하는건 숫자가 아닌 문자 1인것
    num = int(num)  # 문자로 받은 '1'을 숫자 1로 변경해주는 것
    
    if num == 1:    # 문자를 숫자로 변경해주지 않으면 if '1' == 1 일때 문자 1은 숫자 1과 같지 않다
        print('회원입력 시작')    
    elif num == 2:
        print('회원검색 시작')
    elif num == 3:
        print('회원수정 시작')   
    elif num == 4:
        print('회원삭제 시작')    
    elif num == 5:
        print('프로그램 종료') 
        break
    else:
        continue    