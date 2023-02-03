n,k = map(int,input().split())


d = [[0] * (n + 1) for _ in range(k+1)]
d[0][0] = 1


for i in range(1,k+1):
    for j in range(n+1):
        d[i][j] = d[i][j-1] + d[i-1][j]
        d[i][j] = d[i][j] % 1000000000


print(d[k][n])

# 6 4
    # 0 1 2 3 4 5 6 = n
# # # # # # # # # #
# 1 # 1 1 1 1 1 1 1
# 2 # 1 2 3 4 5 6 7
# 3 # 1 3 6 10 15 21 28
# 4 # 1 4 10 20 . . . . . ...
# =
# k
#d[1][1] = d[0] + j[0]














