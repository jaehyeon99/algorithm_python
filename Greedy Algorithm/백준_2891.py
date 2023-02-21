n,s,r = map(int,input().split())
loss = list(map(int,input().split()))
add = list(map(int,input().split()))
result = 0




for i in loss:
    if i in add:
        add.remove(i)
        loss.remove(i)

for i in loss:
    if i-1 in add:
        add.remove(i-1)
    elif i+1 in add:
        add.remove(i+1)
    else:
        result += 1

print(result)


