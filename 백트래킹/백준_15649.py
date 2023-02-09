import itertools

n, m = map(int, input().split())
number =[]
for i in range(1,n+1):
    number.append(i)

array = itertools.permutations(number, m)

for i in array:
    for j in i:
        print(j, end = ' ')
    print()