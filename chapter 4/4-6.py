# lambda 함수 
# 자바스크립트에서는 쉽게 화살표 함수, 익명 함수로 사용 된다.
# 파이썬에서는 람다 함수라고 함수를 간단하게 사용 할 수 있는 방법이 있다.

myList = [lambda a, b : a + b, lambda a, b : a * b]

print(myList[1](1,2))