class Family : 
    lastname = "김"
    # 클래스 변수에 김이라고 적어둠.

Family.lastname = "박"
# 설계도.lastname 을 이용하여 설계도 자체의 변수를 변경 할 수 있다.

print(Family.lastname)

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)