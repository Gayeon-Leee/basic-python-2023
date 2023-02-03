# 모듈 확인

print(f'code29_module_name_review : {__name__}') # __main__ 출력 => entry point(프로그램이 시작하는 시작점)

# if __name__ == '__main__': # => 조건문을 주석처리하면 code30에서 print('name을 실행합니다!!') 실행됨 => main 이라는 조건이 참일때 실행하는 조건문이기 때문
#     print('name을 실행합니다!!')    #code30에서 실행하면 이 부분 실행 안됨 => code30에서는 더이상 __main__ 이 아니기 때문


#print(f'code29_module_name_review : {__name__}')

def add(x, y):
    return x + y
if __name__ == '__main__':
    print('name을 실행합니다!!')
    print(add(3, 4))