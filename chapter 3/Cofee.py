# Coffee.py

coffee = 10

while True :
    money = int(input("돈을 넣어주세요 : "))
    if money == 300 :
        print("[알림] 커피가 나옵니다.")
        coffee = coffee -1
    elif money > 300 :
        print("[알림] 거스름돈 %d를 주고 커피가 나옵니다." % (money - 300))
        coffee = coffee -1
    else :
        print("[알림] 돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("[알림] 자판기 안에 남은 커피의 갯수는 '%d'개 입니다." % coffee)
    if coffee == 0 :
        print("[알림] 커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break