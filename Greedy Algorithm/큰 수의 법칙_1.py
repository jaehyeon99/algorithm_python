n, m, k = map(int, input().split())
arr = list(map(int,input().split()))

arr.sort()

first = arr[n-1]
second = arr[n-2]
result = (((first * k) + second) * (m // (k+1))) + ((m % (k+1))*first)

print(result)
