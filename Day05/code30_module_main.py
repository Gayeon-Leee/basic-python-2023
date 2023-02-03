import code29_module_name   # import 가 module을 불러옴
# __name__ 은 이름 알려주는 것=> code29 파일에서는 __main__ 이었지만 불러오면서 모듈이름이 됨

print(f'code30_module_main : {__name__}')

# C int main(void) 동일
if __name__ == '__main__':
    print('main을 실행합니다!!')
