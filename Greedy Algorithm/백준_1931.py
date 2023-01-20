from sys import stdin

read = stdin.readline

N = int(read())
heap = []
result = []
for _ in range(N):
    a, b = map(int, read().split())
    result.append((a, b))


# result = sorted(result, key=lambda x: x[1])
#
# print(result)
sorted(result, key=lambda x: x[0])
sorted(result, key=lambda x: x[1])
# print(result)



# result = sorted(result, key= lambda x :(x[1],x[0]))

count, last = 0, 0
for start, end in result:
    if start >= last:
        count += 1
        last = end
print(count)
#
