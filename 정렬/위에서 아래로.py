n = int(input())
arr = []
for i in range(n):
    temp = int(input())
    arr.append(temp)

arr.sort(reverse=True)

for i in arr:
    print(i, end=' ')