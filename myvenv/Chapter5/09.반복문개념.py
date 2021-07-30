# 반복문
# : 반복해서 명령을 사요하고 싶을 떄

# 시퀀스 자료형
# : 순서가 있는 자료형
# 1. 리스트
# 2. 문자열
# 3. range 객체
# 4. 튜플
# 5. 딕셔너리

# for 문
# - 리스트 사용
champions = ["티모", "이즈리얼", "리신"]

for champion in champions:  # champions (s 붙어있는게 리스트 자료형)
    print("선택한 챔피언은", champion, "입니다.")

# - 문자열 사용 * 한글자 한글자르 출력해준다.
fighting_message = "자신감을 가지자! 나에게 한꼐란 없다!\n"

for word in fighting_message:
    print(word)

# - range 객체 사용
# range(10) -> 0~9까지 숫자를 포함하는 range 객체나온다. 0,1,2,3,4,5,6,7,8,9

# for i in range(10):
    # print(i)

# range(시작, 끝+1)
# for i in range(1, 10):
    # print(i)

# range(시작, 끝+1, 단계)
for i in range(1, 10, 2):
    print(i)
