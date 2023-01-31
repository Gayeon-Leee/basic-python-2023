# 연산자
# 할당연산 assignment
# 2 = 1   = 은 변수에 값을 집어넣겠다는 의미임 => 2라는 숫자에 1이라는 값을 넣을 수 없어 오류인 것
val = 1 # 마찬가지로 1 = val 은 오류. 왼쪽에 오른쪽 값을 넣는 것이기 때문

# equal 연산자
print(1 == 1)   # True, False 따지는데 가장 중요한게 equal 연산자 '=='

# 사칙연산
print(1 + 1)
print(1 - 1)
print(10 * 10)
print(1024 / 2)     #소수나누기
print(1024 // 2)    #정수나누기
print(4 // 3)
print(4 % 3) # 나누기에서 값을 뺀 '나머지' => 3%3 하면 0 출력됨

# print(6 / 0) 값이 무한대이기 때문에 컴퓨터에서는 6을 0으로 나눌 수 없음
# print(6 // 0) 마찬가지. Python 에서는 zero division error 라고 부름 (언어마다 부르는건 상이)

print(2 ** 10) # 2의 10승

# 문자열연산
first = 'Hello'
second = 'World'
print(first + second)
print(first, second)    #문자 사이에 간격을 두고싶을때 이렇게 해도 되지만 연산을 사용하는 것은 아님
print(first + ' ' + second) #' '(공백)을 두어 세개의 문자열을 더하는 것 => 출력하면 중간에 띄워져서 보임

print(first * 4)    #문자열 연산은 더하기와 곱하기만 가능

#문자열 길이
print(len(first))   
# print(first[0])
# print(first[1])
# print(first[2])
# print(first[3])
# print(first[4]) # 여기에서 []가 배열(list)
# print(first[5]) IndexError

#Python 에서 index를 찾는 특이한 방법.. -가 뒤에서부터 찾아가는것 의미 (다른 언어에서는 안될 수도)
print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])
# print(first[-6]) IndexError

#리스트 자르기 (list split)
current = '2023-01-31 15:24:02' # 현재시간
print(len(current))
print(current[0:4]) #0번째 자리부터 4번째 자리 전까지만 출력(0번부터 3번까지인 2023 출력)
print(current[5:7])
print(current[8:10])
print(current[11:13])
print(current[14:16])
print(current[17:])

print(current[0:4] + '년' + current[5:7] + '월' + current[8:10] + '일' +
      current[11:13] + '시' + current[14:16] + '분' + current[17:] + '초')  #이런 형태로도 가능

print(current[-19:-15]) # -로 찾아가는 것도 된다

# 리스트 연산
que = [1, 2, 3, 4, 5]
que[0] = 7

print(que)  # 리스트는 값을 수정

# que[5] = 10 que의 길이는 5로 index 가 4까지 있기 때문에 5는 안되는 것
# print(que)

que.append(10)  # append는 값을 마지막에 추가
print(que)

que.insert(3, 99)  # insert는 원하는 index에 값을 삽입 
print(que)

que.remove(99)  # remove 원하는 값을 삭제
print(que)

# tup = (1, 2, 3, 4, 5)
# tup[1] = 9

# print(tup)  튜플은 안됨

# 문자열 리스트 == 문자 리스트
title = 'python'
print(title)
print(title[0])

# title[0] = 'P'
# print(title[0]) 문자열에서는 값변경X
print('P' + title[1:])  # => 값 변경이 안되기 때문에 P를 넣고 title 1번째 자리인 y부터 출력하는 것

# 일반적인 문자형 list
text = ['p', 'y', 't', 'h', 'o', 'n']
print(text)
text[0] = 'P'
print(text)

# 문자열 포맷팅
print("I'm so happy {0} you!!".format(2))    #숫자 2가 포맷팅 되어 0번째 자리에 들어가서 문자 2로 출력된것
print("I'm so happy {0} you, {1}!!".format(2, 'Hey'))  #들어갈 자리를 추가할 수도 있고 ''로 문자도 넣을 수 있음  but 둘다 구식

#최신식 문자열 포맷팅
preword = 2
sayHello = 'Hey'
print(f"I'm so happy {preword} you, {sayHello}!!")  #preword, sayHello 자리에 값을 바꾸면 바꾼 값 출력되는 것 => 포맷팅

pi = 3.141592
print(f'파이는 {pi}입니다.')
print(f'파이는 {pi:0.2f}입니다.')   # 0.2f는 소숫점 2번째자리까지만 출력하라는 의미임
print(f'파이는 {pi:10.3f}입니다.')  # 10.3 은 소숫점 앞은 10자리로 , 소숫점은 3번째 자리까지만 출력하라는 의미 _ 소숫점은 반올림

#문자열을 특정 문자로 자르기 => 자주 사용함
full_name = 'Ronald B. Weasely'
vals = full_name.split()    # 공백, 즉 space 기준으로 자르는 것
print(type(vals))
print(vals)

vals = full_name.split('.') # 지정한 . 기준으로 자르는 것
print(vals)

#문자 값 변경
print(full_name.replace('Ronald B.', 'Ron'))    

# 문자열 공백 없애기 _ 공백도 하나의 값 =>공백이 있으면 문제가 생길 수 있기 때문에 공백 없애주는 것
hi = '          Hello~ Bye~          '
print(hi.lstrip() + '|')  #왼쪽 공백 삭제 _ |(pipe) 추가해서 공백 확인한 것임
print(hi.rstrip() + '|')  #오른쪽 공백 삭제
print(hi.strip() + '|')

# 문자열에서 값 찾기
print(full_name.index('B')) #full_name에서 B의 자리 찾는 것
# print(full_name.index('Z')) 없는 값을 찾으면 오류 생김

print(full_name.find('Z'))  # 찾는 값이 없으면 -1 로 출력됨
print(full_name.find('B'))  # 값 찾을 때는 index 보다 find가 좋음.. 없는 값도 오류 없이 -1로 출력되기 때문

#찾는 단어의 개수
print(full_name.count('a'))

#모든 단어를 대문자/소문자로 변경
print(full_name.upper())
print(full_name.lower())

# 연산자 우선순위 // 우선순위 전체를 외운다기 보다는.. 개념 알고.. ()로 우선순위 줄 수 있는 것 알아야함
print(3 + 4 * 2)
print((3 + 4) * 2)  # 원래 * 가 우선순위. 더하기에 우선순위 주기 위해 소괄호() 사용하는 것