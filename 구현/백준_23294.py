from collections import deque

N, Q, C = map(int,input().split())
size = list(map(int, input().split()))
p = 0
total = 0
f = deque()
b = deque()


for _ in range(Q):
    click = list(map(str,input().split()))

    if click[0] == 'B':
        if len(b) != 0:
            f.append(p)
            p = b.pop()


    if click[0] == 'F':
        if len(f) != 0:
            b.append(p)
            p = f.pop()





    if click[0] == 'A':
        total = int(total) - sum([size[int(i)-1] for i in f])
        f.clear()
        p = click[1] # 현재 페이지는 새로 들어온 접속된 페이지가 된다.
        total = total + size[int(click[1]) -1]
        if p != 0:  # [b] deque가 비어 있지 않을 때 추가 해준다.
            b.append(p)

        while total > C:
            temp = list(b).pop(0)
            total = total - size[int(temp)-1]


    if click[0] == 'C':
        for i in range(1,N+1):
            cnt = b.count(i)
            if (cnt > 1):
                for j in range(cnt - 1):
                    total -= size[i - 1]
                    b.remove(i)



print(p)
if len(b) == 0 :
    print(-1)
else:
    print(*list(b))

if len(f) == 0 :
    print(-1)
else:
    print(*list(f))

