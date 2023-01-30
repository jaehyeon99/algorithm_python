n = int(input())
arr = []
for i in range(n):
    temp = input().split()
    arr.append((temp[0],int(temp[1])))

arr.sort(key=lambda student:student[1])

for i in arr:
    print(i[0], end=' ')