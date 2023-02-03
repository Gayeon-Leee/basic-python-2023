# 파일 읽어오기
file = open('./Day05/sample05.txt', 'r', encoding='utf-8')

while True:
    text = file.read()

    if not text: break

    print(text)

file.close() # => 파일 오픈하면 반드시 close 해야함

# text = file.read()
# print(text)

# text = file.read()
# print(text)

# text = file.read()
# print(text) => 이런 식으로 여러 줄 적어서 반복 출력하는걸 for문으로 사용하는 것!

