n, k = map(int, input().split())
coin_type = []
count = 0

for i in range(n):
    price = int(input())
    coin_type.append(price)

coin_type.sort(reverse=True)

for i in coin_type:
    count += k // i
    k = k % i

print(count)



