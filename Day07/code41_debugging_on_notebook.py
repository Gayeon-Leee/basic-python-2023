# %% [markdown]
# # 주피터 노트북 사용법 학습
# 
# ## 마크다운, 파이썬 셀을 추가 : 단축기
# - 현재 셀 앞에 셀추가 : a
# - 현재 셀 뒤에 셀 추가 : b
# - 현재 셀을 마크다운으로 변경 : 포커스만 있는 상태(커서가 깜빡거리지 않는 상태 - esc)에서 m
# - 현재 셀을 코드 셀로 변경 : 포커스 상태에서 y

# %%
# 최초 작성된 Python  셀

# %% [markdown]
# ## 파이썬 셀 실행
# - 셀 실행 : Ctrl + Enter
# - 셀 실행, 다음 셀로 이동, 없으면 생성(이전 셀과 같은 성질의 셀 생성함) : Shift + Enter
# - 셀 실행, 무조건 다음 셀 생성(이전 셀과 같은 성질의 셀 생성함) : Alt + Enter
# - 주석처리 : Ctrl + / 또는 Ctrl + k,c

# %%
print('Hello, Jupyter!!')

# %% [markdown]
# ## 디버깅
# 아무리 강조해도 지나치지 않는 ,,
# 주피터 노트북에서 디버깅 할 때는 제약사항 있음

# %%
arr = [1, '2', True, 'Hello', 3.1415926585]

for i in arr:
    print(i)

# %% [markdown]
# ### 함수 디버깅

# %%
def plus(x, y):
    val = x + y
    return val

def div(x, y):
    val = x / y
    return val

print('더하기')
print(plus(10,4))

# %%
print('나누기')
# print(div(10,0))

# %%

print(arr)
arr

