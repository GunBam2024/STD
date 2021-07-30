# 1. 리스트 만들기
# - 데이터가 있는 리스트
animals = ["가물치", "벼메뚜기", "비단뱀", "도룡뇽"]

# - 데이터가 없는 리스트
empty = []

# 2. 리스트 조작하기

# - 데이터 접근하기
# 인덱스는 0 부터 시작
print(animals[2])
print(animals[-1])  # -1은 마지막 자료를 출력해준다.

# - 데이터 추가하기
animals.append("고라니")
print(animals)

# - 데이터 할당하기(변경하기)
animals[1] = "청개구리"
print(animals)

# - 데이터 삭제하기
del animals[0]
print(animals)

# - 리스트 슬라이싱 끝은 인덱스로 +1로 계산해서 적어줘야된다.
print(animals[1:3])
print(animals[:])  # 전체 (이부분은 가물치는 제거가 된곳이다.)
print(animals[:3])  # 고라니만 빠진 상태로 출력 된다.
print(animals[1:])  # 첫번째 뺴고 마지막까지 출력

# - 리스트 길이
print(len(animals))

# - 리스트 정렬
animals.sort()  # 오름차순
# animals.sort(reverse=True)  # 내림차순(역순) sort안에 reverse=True 넣으면 된다.
print(animals)
