class FourCal :
    def __init__ (self, first, second) :
        self.first = first
        self.second = second
    # __init__ : 특별한 함수이다. 아래에 있는 일반적인 함수우ㅘ 변수와 다르게
    # class를 처음 만들 때 init : 처음 시작하다의 영어
    # FourCal() 클래스로 찍어내서 결과를 만들 때
    # __init__ 을 처음으로 무조건 실행하게 된다.

    # __init__ : 생성자라고 한다. 가장 처음으로 구성해주는 것 즉 생성자이다.

    def setdate(self, first, second) :
        self.first = first
        self.second = second

    def add(self) :
        result = self.first + self.second
        return result

# a = FourCal()
# 이렇게 바로 돌릴시 a를 인스턴스라고 한다. -> 생성자를 실행할려면 first 와 second 이러한 객체들을 넣어서 실행시켜줘야 오류가 안 뜬다.

## 상속 개념 시작

class SafeFourCal(FourCal) :
    def div(self) :
        if self.second == 0 :
            return 0 
        else :
            return self.first / self.second
