# 시퀀스 자료형
# : 순서가 있는 자료형
# 1. 리스트
# 2. 문자열
# 3. range 객체
# 4. 튜플
# 5. 딕셔너리

# for 문
# - 리스트 사용
cr = ["티모", "이즈", "리신"]

for c in cr:
    print("선택한 챔피언은", c, "입니다.")

# - 문자열 사용
f = "자신감"

for ft in f:
    print(ft)

# - range 객체 사용
# range(10) -> 0~9까지 숫자를 포함하는 range 객체나온다. 0,1,2,3,4,5,6,7,8,9
# for i in range(10):
#     print(i)

# range(시작, 끝+1)
# 쉽게 말해 시작은 1이상이고 끝은 "10미만" 이다. 미만이기에 +1하는 것이다.
# range(dt1, dt2, dt3) dt == data dt1은 시작 dt2는 끝(미만) dt3은 배열배수출력
# for i in range(1, 10):
#     print(i)
# index 는 0부터 시작 2,4,6 으로 가기때문에 출력은 인덱스로 보면 1,3,5,7,9 이다.
for i in range(1, 10, 2):
    print(i)

# while문
# : 보통 반복 횟수가 정해지지 않았을 때 사용한다.

# i = 0  # 초기식
# while i <= 10:
#     print(f"{i}번째 다짐, 나는 할수 있다.")
#     i += 1  # 증감식

while True:
    x = input("종료 하려면 exit를 입력해라 >>>")
    if x == "exit":
        break
