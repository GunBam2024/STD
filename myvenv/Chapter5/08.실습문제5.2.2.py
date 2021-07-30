# 실습문제 5.2.2

data = []  # 빈 리스트 생성

# x = int(input("1일차 턱걸이 횟수 >>>"))
# data.append(x)
# x = int(input("2일차 턱걸이 횟수 >>>"))
# data.append(x)
# x = int(input("3일차 턱걸이 횟수 >>>"))
# data.append(x)
# x = int(input("4일차 턱걸이 횟수 >>>"))
# data.append(x)
# x = int(input("5일차 턱걸이 횟수 >>>"))
# data.append(x)
# x = int(input("6일차 턱걸이 횟수 >>>"))
# data.append(x)
# x = int(input("7일차 턱걸이 횟수 >>>"))
# data.append(x)

# 반복문
# range(data1, data2) data1은 시작 1번 data2는 7+1까지 (슬라이딩 처럼 마지막 +1해줘야됨)
# 예로 들어 1이상 8미만 이라 생각하면 된다.
# 미만일경우 8은 포함되지 않기때문에 7일까지 나온다.
for i in range(1, 8):
    x = int(input(f"{i}일차 턱걸이 횟수 >>>"))
    data.append(x)

total = data[0] + data[1] + data[2] + data[3] + data[4] + data[5] + data[6]
avg = total / 7
# 이곳에서 오류 많이난다 "IndexError : list index out of range" 리스트 인덱스가 넘어갔다라는 오류
print(int(avg))
