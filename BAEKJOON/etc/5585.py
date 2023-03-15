money = 1000 - int(input())
coin = [500, 100, 50, 10, 5, 1]
n = 0
for i in coin:
    n += money // i
    money %= i
print(n)