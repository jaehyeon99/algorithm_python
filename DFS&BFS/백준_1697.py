# import sys
# from collections import deque
#
# def bfs(v):
#     q = deque([v])
#     while q:
#         v = q.popleft()
#         if v == k:
#             return array[v]
#         for next_v in (v-1, v+1, 2*v):
#             if 0 <= next_v < MAX and not array[next_v]:
#                 array[next_v] = array[v] + 1
#                 q.append(next_v)
#
#
# MAX = 100001
# n, k = map(int, sys.stdin.readline().split())
# array = [0] * MAX
# print(bfs(n))

from collections import deque
import sys

def bfs(v):
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        if v == k:
            return visited[v]
        for i in (v + 1, v - 1, v * 2):
            if 0 <= i < max and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)

max = 100001
n, k = map(int, sys.stdin.readline().split())
visited = [0] * max
print(bfs(n))


