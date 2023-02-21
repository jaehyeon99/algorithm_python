n = int(input())
target = list(input())
answer = 0

for i in range(n-1):
    compare = target[:]
    word = input()
    cnt = 0

    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt = cnt + 1

    if cnt < 2 and len(compare) < 2:
        answer = answer +1

print(answer)
