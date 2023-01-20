n = input()
row = int(n[1])  # 숫자 [1]
column = int(ord(n[0])) - int(ord('a')) + 1  # 알파벳 [0]
result = 0
#97이 a
# print(column)
# 이동 가능한 경우
# 1. 수평으로 두 칸 이동 뒤에 수직으로 한 칸 이동하기
# 2. 수직으로 두 칸 이동 뒤에 수평으로 한 칸 이동하기

can_move = [(2,-1),(2,1),(-2,-1),(-2,1),(1,2),(1,-2),(-1,2),(-1,-2)]


for i in can_move:
    next_cols = column + i[0]
    next_rows = row + i[1]

    if next_rows>= 1 and next_rows <= 8 and next_cols >= 1 and next_cols<= 8:
        result += 1

print(result)
