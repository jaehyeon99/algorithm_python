# N = int(input())
# x,y = 1,1
# move = input().split()
#
# for i in move:
#     if i == 'R':
#         if y == N:
#             y  = y
#         else:
#             y = y +1
#     elif i == 'U':
#         if x == 1:
#             x = x
#         else:
#             x = x-1
#     elif i == 'D':
#         if x == N:
#             x = x
#         else:
#             x = x + 1
#     elif i == 'L':
#         if y == 1:
#             y = y
#         else:
#             y = y - 1
# print(x , y)

n = int(input())
x, y = 1,1
plans = input.split()

# type 에 따른 좌표 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        x,y = nx, ny
print(x,y)