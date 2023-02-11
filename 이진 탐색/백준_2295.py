n = int(input())
u = set()
ans = []
for i in range(n):
    u.add(int(input()))  # tuple 에 데이터 삽입할 때는 add 사용

sums = set()
for i in u:
    for j in u:
        sums.add(i+j)


test = set()

for i in u:
    for j in u:
        if (j-i) in sums:
            ans.append(j)




print(max(ans))