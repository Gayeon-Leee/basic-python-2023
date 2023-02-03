# 공공데이터포털 csv파일 읽기
# 부산광역시 시내버스, 마을버스 현황
import csv

fileName = 'busanbus.csv'
dirName = 'C:/Source/studyPython2023/' # 주소 복사만 하면 마지막 2023 옆에 / 없음. 이 폴더 밑에 있는 파일이기 때문에 / 꼭 넣어줘야함.
fullPath = dirName + fileName

file = open(fullPath, 'r', encoding='utf-8')
reader = csv.reader(file, delimiter=',')
next(reader)

for line in reader:
    print(line)

file.close() # 닫는거 필수!!
