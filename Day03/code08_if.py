# if문
name = 'Ron'
state = '안아픔'

if name == 'Ron' :  #if문에서 : 안쓰면 error / 같다는 ==, 같지 않다는 != / != 일때는 이름이 Ron이 아닌 경우에 True가 되는 것임
    print('진료실에서 담당의사를 만납니다.')    # name == Ron 의 경우, 이름이 Ron인 것이 True면 if문 출력
    if state == '아픔' :    # if문 안에도 if문 또 적을 수 있음
        print('선생님, 아파요')
        print('어디가 어떻게 아프십니까?')
    else:
        print('어디가 아프십니까?')
        print('안아픈데요')
        print('그럼 왜 오셨어요?')    
elif name == 'Hermione' :   # else 외의 또 다른 조건
    print('주사실로 갑니다.')
    print('팔 걷으세요~')
else:
    print('조용히 기다립니다.')     # name == Ron 의 경우, name이 Ron인 것이 False면 else 출력