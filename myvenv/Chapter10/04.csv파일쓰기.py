import csv

data = [
    ["이름", "반", "번호"],
    ["재석", 1, 20],
    ["홍철", 3, 8],
    ["형동", 5, 32]
]

# windows 사용자는 newline=""자동으로 한줄씩 떨어지는 것을 막는 코드이다.
# windows 사용자는 encoding="utf-8-sig" 사용해야 vs코드에서 csv가 깨지지 않는다.
file = open("./myvenv/Chapter10/student.csv",
            "w", newline="", encoding="utf-8-sig")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)

file.close()
