a = 1
def vartest():
    global a
    #global a = 즉 밖에 있는 전역변수라는 개념이다.
    #여기서만 쓰이는 변수가 아니고 global을 쓰게 되면 전체에서 사용 할 수 있는 변수가 된다.
    a = a + 1

vartest()
print(a)