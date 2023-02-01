# 전역/지역변수
# 함수가 없을 때는 local과 global의 차이가 없음. 함수를 쓰면 local 과 global 이 달라진다 => 함수(지역)안의 변수가 locals

num = 1

for i in range(1, 11):
    num = i * num
    print(f'{i + 1}번')

    if i % 3 == 0: # 3의 배수
        res = '테스트'
        print(res)

print(f'결과 {num}')
print(res)       