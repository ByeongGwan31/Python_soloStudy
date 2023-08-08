#mod1.py

def add(a,b) :
    return a + b

def sub(a,b) :
    return a - b

if __name__ == "__main__" :
    # __name__ : 지금 실행하는 함수의 이름이다.
    # hello.py의 이름이 __main__이 된다.

    # 만약 __name__ 이 __main__이어야만 밑에를 실행한다.
    print(add(1, 4))
    print(add(4, 2))

    # 내가 실행하는 파일 이름이 main이다. 그 파일에서만 실행 할 수 있다.