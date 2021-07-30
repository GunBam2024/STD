# 튜플
# : 읽기 전용 리스트
a = (3, 4, 5)
b = 3, 4, 5

c = (3,)
d = 3,

# 튜플 리스트 자료형변환
e = tuple([3, 4, 5])
f = list(range(10))
g = tuple(f)

# 튜플을 리스트로 바꾸어서 저장
h = 3, 4, 5
i = list(h)

# 튜플 관련 함수
x = 5, 6, 7, 8
print(max(x))
print(min(x))
print(sum(x))
print(x.count(6))
print(x.index(7))
