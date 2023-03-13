N = int(input())
score = list(map(int, input().split()))
score_max = max(score)
print(((sum(score)*100)/score_max)/N)