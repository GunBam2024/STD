# 원화를 입력, 환율 입력 -> 달러값

won = input("원화금액을 입력 하세요>>>")
dollar = input("환율을 입력 하세요>>>")

try:  # 예외가 발생 할 수 있는 코드
    print(int(won) / int(dollar))
except ValueError as e:  # 예외가 발생햇을 때 실행되는 코드
    print("예외가 발생햇습니다.", e)
except ZeroDivisionError as e:
    print("예외가 발생햇습니다.", e)
else:
    print("예외가 발생하지 않았을 때 실행되는 코드")
finally:  # 파일 닫기 리소스 반환을 꼭해줘야되는 거에 쓴다.
    print("예외가 발생하던지, 발생하지 않더지 나오는 코드")
