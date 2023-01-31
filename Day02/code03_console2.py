# 콘솔출력 - 엔터를 공백으로 변경 
print('*')
print('**')
print('***')
print('****')
print('*****') # 이렇게 작성하면 각 한줄씩 총 5줄 출력됨

print('*', end=' ')
print('**', end=' ')
print('***', end=' ')
print('****', end=' ')
print('*****')  #end=' ' 넣어서 한줄로 출력
# parameter end에 공백을 주면 enter 대신 space로 변경되어 출력되는 것 => 한 줄로 출력

# 공백구분자를 /로 변경
print('a', 'b', 'c', sep='/')