n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
visited = [[0] * m for _ in range(n)]

# 북,동,남,서
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]


def turn_Left():
    global d
    d = d - 1
    if d == -1:
        d = 3


cnt = 1
turn_time = 0

while True:
    turn_Left()
    nx = r + dx[d]
    ny = c + dy[d]
    if graph[nx][ny] == 0 and visited[nx][ny] == 0:
        # 다시 방문하지 않도록 방문처리.
        visited[nx][ny] = 1
        cnt = cnt + 1
        r, c = nx, ny
        turn_time = 0
        continue
    else:
        turn_time = turn_time + 1
    if turn_time == 4:
        nx = r - dx[d]
        ny = c - dy[d]

        if graph[nx][ny] == 0:
            r, c = nx, ny
        else:
            break
        turn_time = 0
print(cnt)





