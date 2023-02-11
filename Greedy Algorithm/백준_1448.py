import sys


n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse=True)

total = -1
for i in range(n-2):
    if arr[i] < arr[i+1] + arr[i+2]:
        total = arr[i] + arr[i+1] + arr[i+2]
        break

print(total)



