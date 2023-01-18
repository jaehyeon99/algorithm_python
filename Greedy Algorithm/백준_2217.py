n = int(input())
arr = list()
for i in range(n):
    data = int(input())
    arr.append(data)

arr.sort(reverse=True)

for i in range(n):
    arr[i] = arr[i] * (i+1)

result = max(arr)

print(result)