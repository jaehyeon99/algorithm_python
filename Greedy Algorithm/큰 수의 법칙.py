# n ,m ,k 입력 받기

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()  # 입력받은 수들 정렬

# 2 4 4 5 6 으로 정렬

first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 k번 더하기
        if m == 0:
            break
        result += first
        m = m-1
    if m == 0:
        break
    result += second # 두 번째로 큰 수 한 번 더해주기
    m = m-1
print(result)
