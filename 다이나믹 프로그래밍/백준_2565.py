n = int(input())
arr = []
for i in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))
arr.sort(key = lambda x:x[0])
dp = [1] * n                                         
for i in range(n):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))