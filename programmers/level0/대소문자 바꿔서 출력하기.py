s = input()
for i in s:
    if ord(i) < 91:
        print(i.lower(), end='')
    else:
        print(i.upper(), end='')