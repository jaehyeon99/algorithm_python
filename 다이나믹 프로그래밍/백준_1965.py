n = int(input())
k = list(map(int,input().split()))
d = [1 for _ in range(n)]
for i in range(1,n):
    for j in range(i):
        if k[i] > k[j]:
            d[i] =  max(d[i],d[j] + 1)

print(max(d))