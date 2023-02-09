n,m = map(int,input().split())
subject = []
point = []
for i in range(n):
    p,l = map(int,input().split())
    subject.append([p,l])
    point.append(list(map(int,input().split())))

a = []
for i in range(n):
    temp = subject[i][0] - subject[i][1]
    a.append(temp)
b=[]
for i in point:
    i.sort()
    b.append(i)
c=[]
d =[]
for i in range(n):
    if a[i] >= 0:
        d.append(b[i][a[i]])
    else:
        d.append(1)

d.sort()
total = 0
count = 0
for i in d:
    if total + i <= m:
        total = total +i
        count = count + 1
print(count)
