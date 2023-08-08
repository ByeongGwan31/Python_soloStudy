# 한 줄이 아니고 모든 줄을 읽으려면 어떻게 해야할까?
# readlines() 사용하기

f = open("새파일.txt", 'r', encoding="UTF-8")

lines = f.readlines()

for line in lines :
    print(line, end = "")
f.close()