l = [] 
for _ in range(6):  
    l.append(int(input())) 
l1 = sorted(l[:4]) 
l2 = sorted(l[4:]) 
print(sum(l1[1:]) + l2[-1])