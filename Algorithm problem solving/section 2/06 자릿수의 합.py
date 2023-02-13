N = int(input())
num = list(map(int, input().split()))
result = []
def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum
max = -2147000000
for x in num:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(res)

'''
def digit_sum(x):
    sum = 0
    for i in str(x):
        sum+= int(i)
    return sum
'''