# from collections import deque
#
# N = int(input())
#
# # 행렬 만들기
# graph = [list(map(int, input())) for _ in range(N)]
#
#
# def bfs(graph, x, y):
#     # 상하좌우
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     queue = deque()
#     queue.append((x, y))
#     graph[x][y] = 0  # 탐색중인 위치 0으로 바꿔 다시 방문하지 않도록 함
#     cnt = 1
#
#     while queue:
#         x, y = queue.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or nx >= N or ny < 0 or ny >= N:
#                 continue
#
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 queue.append((nx, ny))
#                 cnt += 1
#     return cnt
#
#
# result = []
# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == 1:
#             count = bfs(graph,i,j)
#             result.append(count)
#
#
#
# result.sort()
# print(len(result))
#
# for i in range(len(result)):
#     print(result[i])

from collections import deque

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))




# 좌 우 상 하

def bfs(graph, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append((x, y))
    cnt = 1
    graph[x][y] = 0
    while q:

        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt = cnt + 1
    return cnt


result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count = bfs(graph, i, j)
            result.append(count)

result.sort()
for i in range(len(result)):
    print(result[i])













