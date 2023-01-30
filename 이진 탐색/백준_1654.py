n,m = map(int,input().split())
arr =[]
for i in range(n):
    arr.append(int(input()))

start = 1
end = max(arr)
result = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in arr:
            total = total + (i // mid)
    if total < m :
        end = mid -1
    else:
        result = mid
        start = mid + 1


print(result)
