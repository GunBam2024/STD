# =================조건문==========
# # 연습 1
# x = int(input("현재 구독자 수 >>>"))

# if x >= 1000:
#     print("수익창출 가능")
# else:
#     print("불가능")

# # 연습 2
# x = int(input("공부시간 입력 >>>"))

# if x >= 10:
#     print("잠금해지")
# elif x >= 5:
#     print("30분")
# else:
#     print("불가능")

# # 연습 3
# x = int(input("내가 가진돈 >>>"))

# if x >= 20000:
#     print("치킨")
# elif x >= 12000:
#     print("떡볶이")
# else:
#     print("편의점")

# # 연습 4
# a = int(input("국어 >>>"))
# b = int(input("수학 >>>"))
# c = int(input("영어 >>>"))

# total = a+b+c
# ag = total/3

# if 0 <= a <= 100 and 0 <= b <= 100 and 0 <= c <= 100:
#     if ag >= 80:
#         print("불합격")
#     else:
#         print("합격")
# else:
#     print("수식이 안맞다")

# ==============반복문===================
# # 연습 1
# x = [33, 40, 12, 63, 52]

# # 추가
# x.append(9)
# print(x)

# # 할당 (수정)
# x[1] = 50
# print(x)

# # 슬라이싱
# print(x[2:6])

# # 오름차순 : 내림차순은 x.sort(reverse=True)
# x.sort()
# print(x)

# 연습 2 (이거 다시연습할것)

d = []

for i in range(1, 8):
    x = int(input(f"{i}일차 턱걸이 횟수 >>>"))
    d.append(x)

total = d[0] + d[1] + d[2] + d[3] + d[4] + d[5] + d[6]
ag = total/7

print(int(ag))
