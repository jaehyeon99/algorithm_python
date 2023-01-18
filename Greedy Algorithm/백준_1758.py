n = int(input())
think =[]
result = 0
count = 1


for i in range(n):
    tip = int(input())
    think.append(tip)


think.sort()
think.reverse()

for origin in think:
    temp = 0
    temp = origin - (count - 1)
    count += 1
    if temp < 0:
        result += 0
    else:
        result += temp

print(result)
