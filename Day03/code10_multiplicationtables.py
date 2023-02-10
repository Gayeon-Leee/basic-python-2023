# 구구단 프로그램

# for y in range(1, 10):
#     print(f'{2} X {y} = {2*y}') # print('2 X 1 = 2')의 형태를 반복할 수 있게 한 것

# for y in range(1, 10):
#     print(f'{3} X {y} = {3*y}')
# 위 처럼 하면 2단부터 9단까지 일일이 작성해야함 => for문의 형태가 같을 때 여러 번 반복해서 작성X

for x in range(2,10):
    print(f'{x}단 시작 ======') 
    for y in range(1,10):
        print(f'{x} X {y} = {x*y:>2}', end=' ') # :>2 는 두자리로 만들어서 오른쪽 정렬하라는 것 => 전체 줄 길이 맞춰줌
    print() # 안쪽 for문이 끝나고 나서 print를 한 번 하게 함으로써 다음거 실행되기 전에 구분을 주는 것 
    # => 디버깅 실행해보면 9단까지 하고나면 여기로 내려왔다가 다시 for문 올라가는거 확인 가능
    