n, k = map(int, input().split())
count = 0

while n != 1:
    if k == 1:
        n = n - 1
        count += 1
    elif k >= 2:
        if n % k == 0:
            n = n / k
            count += 1
        else:
            n = n - 1
            count += 1

print(count)

