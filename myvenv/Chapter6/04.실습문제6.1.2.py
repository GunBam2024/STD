# 실습문제6.1.2

def printSumAvg(x, y, z):
    """
    세개의 숫자를 받아 합계와 평균을 출력하는 함수
    """
    sum = x + y + z
    avg = sum / 3
    # print("합계 :", sum, "평균", avg) 콤마안찍고 앞에 f넣어주면된다.
    print(f"합계 : {sum} 평균 : {avg}")


printSumAvg(10, 20, 30)
