n = int(input())
p = list(map(str, input().split()))
sum = 0
res = 0
for i in range(len(p)):
    sum = sum + int(p[i])
res = sum / n
print(res)
