# 한 줄이 아니고 모든 줄을 읽으려면 어떻게 해야할까?

f = open("새파일.txt", 'r', encoding="UTF-8")

while True :
    line = f.readline()
    if not line : break
    print(line)

f.close()