n = int(input())
k = list(map(int, input().split()))
result = 0

k.sort()

for i in range(n):
    result = result + sum(k)
    k.pop()


print(result)