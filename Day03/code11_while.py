# while문
hit = 0 # 변수 초기화 중요함 / 초기화시키기 않으면 None 으로 보기 때문에 숫자로 인지할 수 있도록 초기화 시켜주는 것

while hit < 101:    # while true: 로 하면 수의 제한 조건이 없기 때문에 무한 반복. 조심해서 쓰기~~
    hit += 1 # hit를 1씩 증가

    print(f'나무를 {hit}번 찍었습니다')
    if hit == 10:       # if, else 없으면 < 101 까지 while문 실행
        print('나무가 넘어갔습니다!')
        break
    else:
        print('나무가 아직 넘어가지 않았습니다.')

print('나무찍기 완료')        