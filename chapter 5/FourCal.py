class FourCal :
    def setdata(self, first, second) :
        self.first = first
        self.second = second
        # 메서드라고 부른다.

    # self => a.setdata(4, 2)   => self => a // 4 => first // 2 => second

    def add(self) :
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(4,2)
print(a.add())