# # 구구단 연습하고 외울것
# x = int(input("몇 단 >>>"))

# for i in range(1, 10):
#     print(f"{x} * {i} = {x*i}")

# #여기도 다시할것
# while True:
#     print("1번 게임시작 2번 랭킹 3번 게임종료")
#     x = int(input("할걸 선택해라 >>>"))

#     if x == 1:
#         print("-> 게임시작")
#     elif x == 2:
#         print("-> 랭킹")
#     elif x == 3:
#         print("-> 종료")
#         break
#     else:
#         print("잘못입력")

# x = ["하하", "두두", "삼삼"]

# i = 0

# for t in x:
#     print(t)
#     d = input()
#     if d == t:
#         i += 1
# print("전체 문제 개수 : ", len(x))
# print("맞힌 개수 : ", i)
# print("틀린 개수 : ", len(t) - i)

# # 전체 문제 개수 : 4 개
# # 맞힌 문제 개수 : 2 개
# # 틀린 문제 개수 : 2 개

x = int(input("몇단 >>"))

for i in range(1, 10):
    print(f"{x}*{i} = {x*i}")
