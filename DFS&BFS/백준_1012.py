from collections import deque

T = int(input())


# 상하좌우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def BFS(graph,x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y]  = 0
    while queue:
        a,b = queue.popleft()
        for i in range(4):
            nx = a +dx[i]
            ny = b+ dy[i]
            if nx<0 or nx >=n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
    return

for i in range(T):
    cnt = 0
    n, m, k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                BFS(graph, a, b)
                cnt += 1
    print(cnt)









# 2
# 10 8 17
# 0 0
# 1 0
# 1 1
# 4 2
# 4 3
# 4 5
# 2 4
# 3 4
# 7 4
# 8 4
# 9 4
# 7 5
# 8 5
# 9 5
# 7 6
# 8 6
# 9 6
# 10 10 1
# 5 5