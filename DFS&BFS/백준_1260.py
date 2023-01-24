from collections import deque

n, m, V= map(int, input().split())
matrix = [[0]* (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    a,b = map(int,input().split())
    matrix[a][b] = matrix[b][a] = 1

def dfs(V):

    visited[V] = 1

    print(V , end = ' ')

    for i in range(1, n+1):
        if (visited[i] == 0 and matrix[V][i] == 1):
            dfs(i)

def bfs(V):

    queue = [V]
    visited[V] = 0
    while queue:
        V = queue.pop(0)
        print(V, end= ' ')

        for i in range(1,n+1):
            if(visited[i] == 1  and matrix[V][i] == 1):
                queue.append(i)
                visited[i] = 0


dfs(V)
print()
bfs(V)







