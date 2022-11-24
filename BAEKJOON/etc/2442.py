n = int(input())

star = '*'
space = ' '

for i in range(n):
    print((space*(n-(i+1)))+(star*((2*(i+1)-1))))

#    *
#   ***
#  *****
# *******
#*********
# 출력 오류가 있었다.
# 별 뒤에는 공백 출력을 안해야한다.