# 실습문제6.1.1
# 함수호출방법

# docstring : 설명문

def multiply(x, y):
    """
    두수의 곱셈 결과를 반환하는 함수
    매개변수 x : 숫자
    매개변수 y : 숫자
    """
    result = x * y
    return result


multiply(3, 4)  # 3,4가 들어가면 오류 발생하지 않으므로 아무것도 안뜬다.

# 객관식 코드에 알맞게 들어가는것은?
# 1번은 값이 없다. 2번 값이 1개이다 3번 정답 4번 문자열은 곱셈안된다.
# 1. multiply() 2. multiply(3) 3. multiply(3,4) 4. multiply("a","b")
