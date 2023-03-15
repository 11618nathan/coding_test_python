train_p = 0
train_max = 0
for i in range(4):
    train_o, train_i = map(int, input().split())
    train_p = train_p - train_o + train_i
    if train_max < train_p:
        train_max = train_p
print(train_max)