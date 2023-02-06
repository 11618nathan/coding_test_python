N = int(input())
str_base = list(input())
for i in range(N-1):
    str_add = list(input())
    for j in range(len(str_base)):
        print(str_base[j])
        if str_base[j] != str_add[j]:
            str_base[j] = '?'
print(''.join(str_base))