N , M = map(int, input().split())
x,y,direction =map(int,input().split())
arr= []

d = [[0] * M for _ in  range(N)]
d[x][y] = 1


for i in range(N):
    arr.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction = direction -1
    if direction == -1: # 북쪽에서 서쪽으로 갈 경우 처리
        direction = 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] == 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time = turn_time+1

        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]

            if arr[nx][ny]  == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0

print(count)