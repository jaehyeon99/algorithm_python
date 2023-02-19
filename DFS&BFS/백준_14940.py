from collections import deque

n,m = map(int,input().split())
mapInfo = []
visited =[[0 for _ in range(m)] for _ in range(n)]
distance=[[-1 for _ in range(m)] for _ in range(n)]
startDot = ()

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(n):
    eachRow = list(map(int, input().split()))
    # map을 만들어줄 때 2이면 시작 포인트를 잡는다.
    for j in range(len(eachRow)):
        if eachRow[j] == 2:
            startDot = (i, j)
    mapInfo.append(eachRow)


def BFS(mapInfo,startDot):
    queue =  [startDot]
    visited[startDot[0]][startDot[1]] = True
    distance[startDot[0]][startDot[1]] = 0
    while queue:
        curN,curM = queue.pop(0)
        for i in range(4):
            newR,newC = curN + dx[i], curM +dy[i]

