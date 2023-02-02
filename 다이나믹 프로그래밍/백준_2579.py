n = int(input())
arr = [0 for _ in range(301)]
for i in range(n):
    arr[i] = int(input())

d =[]

if n > 2:
    d.append(arr[0])
    d.append(arr[0]+arr[1])
    d.append(max(arr[0]+arr[2], arr[1]+arr[2]))

    for i in range(3,n):
        d.append(max(d[i-2],d[i-3]+arr[i-1])+arr[i])

    print(d[n-1])

else:
    if n == 1:
        print(arr[0])
    else:
        print(arr[0] +arr[1])
