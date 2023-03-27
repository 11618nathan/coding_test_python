str = input()
result = []
for i in str:
    if ord(i) < 91:
        i = ord(i) + 32
        i = chr(i)
        result.append(i)
    else:
        i = ord(i) - 32
        i = chr(i)
        result.append(i)
    
for i in result:
    print(i, end='')