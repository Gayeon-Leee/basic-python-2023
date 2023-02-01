# 라이프 스코프
a = 1   # 여기서 a는 전역변수 

def vartest(a): # 여기서 a는 매개변수 / 지역변수(locals) => 위의 변수 a와 다름 // 헷갈리면 매개변수 a 대신 x 넣는다고 생각하기
    a = a + 1
    return a

a = vartest(a)
print(a)


def vartest(): 
    global a    # => 함수 안에서도 지역변수(locals) a를 사용하지 않고 전역변수(globals) a를 쓰겠다는 것
    a = a + 1
    return a

a = vartest()
print(a)
# 위에서는 전역변수와 지역변수 a가 다르기 때문에 x를 사용하지 않고 a를 사용해도 문제가 없지만 globla a를 쓰겠다고 선언하면
# vartest(a)를 둘 수 없음. 어느 a 인지 인지하지 못하기 때문 => 이 형태로 사용하거나 x 로 써야한다