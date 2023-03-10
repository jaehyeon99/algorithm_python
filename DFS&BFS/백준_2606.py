# n = int(input())
# s = int(input())
# graph = [[0] * (n+1) for _ in range(n+1)]
# visited = [0] * (n+1)
# for i in range(s):
#     a,b = map(int,input().split())
#     graph[a][b] = graph[b][a] = 1
#
# def dfs(x):
#     visited[x] = 1
#     for i in range(1,n+1):
#         if( visited[i] == 0 and graph[x][i] == 1):
#             dfs(i)
#     count = visited.count(1)
#     return count - 1
#
# print(dfs(1))
#
#
#
#

from collections import deque

n = int(input())
s = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for i in range(s):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def BFS(x):
    q = deque([x])
    count = 0
    visited[x] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                count = count + 1
    return count


print(bfs(1))







