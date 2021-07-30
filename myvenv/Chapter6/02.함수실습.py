# 기본형

# 1. 정의하기
import random


def printHello():
    print("Hello")


# 2. 호출하기
printHello()

# 매개변수가 있는 함수


def sum(a, b):
    print(a + b)


sum(3, 4)

# 반환값이 있는 함수  *random을 사용하기위해 import random 을 해주야된다.


def getRandomNumber():
    number = random.randint(1, 10)
    return number


print(getRandomNumber())

# 매수변수와 반환값이 있는 함수


def add(a, b):
    result = a + b
    return result


print(add(5, 6))
