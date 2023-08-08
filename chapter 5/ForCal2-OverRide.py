class FourCal :
    def __init__ (self, first, second) :
        self.first = first
        self.second = second
    
    def setdata (self, first, second) :
        self.first = first
        self.second = second
    
    def add(self) :
        result = self.first + self.second
        return result

    def mul(self) :
        result = self.first * self.second
        return result

    def sub(self) :
        result = self.first - self.second
        return result

    def div(self) :
        result = self.first / self.second
        return result

class SafeFourCal(FourCal) :
    def div(self) :
        if self.second == 0 :
            return 0
        else :
            return self.first / self.second

## 한번 더 정의한 나누기이다. 부모에 있는 메서드도 있고 자식에 있는 메서드도 있다.
# 이렇게 시작되면 부모 이기는 자식 없다. 하면서 결국 자식이 먼저 실행된다.
# 자기만의 클래스를 만들기 위해서 상속을 실행한다.
# 똑같이 쓰면 변형을 할 수 있다.
## -> 0으로 나누면 안되니깐 -> 0이 아니면 나눠라

a = SafeFourCal(4, 2)
print(a.div())
