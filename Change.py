
# 거스름돈 알고리즘

n = 11618
count = 0

coin_types = [500, 100, 50, 0]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)
