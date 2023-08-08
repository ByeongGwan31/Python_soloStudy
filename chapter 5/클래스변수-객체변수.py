class FourCal :
    first = 2
    second = 3
    # -> 클래스 변수 
    # -> 클래스의 공통적으로 적용되는 변수이다.


    # def __init__ (self, first, second) :
    #     self.first = first
    #     self.second = second
    ## -> 객체변수라고 불린다.
    
    def setdata (self, first, second) :
        self.first = first
        self.second = second
    
    def add(self) :
        result = self.first + self.second
        return result 

a = FourCal()
print(a.first)
b = FourCal()
print(b.first)