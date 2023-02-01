# for 문
arr = [1,2,3,4,5]
sum = 0

for item in arr:
    print(item)
    sum += item     # sum = sum + item 의 의미

print('합계는', sum)    # for문 밖에 있는 거


# 리스트를 편하게 만드는 방법
vals = [i for i in range(1, 11)]    # [1,2,3,4,5,6,7,8,9,10] 의미의 구문. 
print(vals)

#continue / break => for문 안에서의 if문에서만 사용.. 그냥 if문에서는 사용할 수 없음
num = 0
for item in vals: 
    num += 1    # for 문을 실행하면서 num에 1씩을 더함
    if num % 2 == 0:    # num을 2로 나눈 나머지가 0 => 짝수
        #continue # 이후의 것을 수행하지 않고 다시 for문으로
        break # break를 만나면 for문을 완전히 탈출 => 2를 만났을때 나머지가 0이 되므로 for에서 탈출한 것
    else:
        print(num, '번 수는', item, '입니다') 



# 복습
# for 변수 in range(횟수):
#   반복할 코드
 
for i in range(10):
    print('Hello world')   


# for 변수 in list
#   수행할 문장    

#연습문제

x = [49, -17, 25, 102, 8, 62, 21]

for n in x :
    print(n * 10, end=' ')
