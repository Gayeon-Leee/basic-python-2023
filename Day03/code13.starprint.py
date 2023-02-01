#별표찍기

print('*')

arr = ['*', '**', '***', '****', '*****']
for item in arr:
    print(f'{item}')    # 내가 한거

for i in range(1, 6):
    print('*'*i)    # 쌤이 보여준 정답

for i in range(5, 0, -1):
    print('*'*i)    # 5부터 1까지 1씩 감소하면서 반복하는 것 

for i in range(1, 6, 1):
    print('*'*i)    # 1부터 5까지 1씩 증가시키면서 반복하는 것