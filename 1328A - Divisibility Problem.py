t = int(input())
num = []
res = []
result = 0
for i in range(0, t):
    ele = list(map(int, input().split()))
    num.append(ele)
for i in num:
    if i[0] % i[1] == 0:
        result = 0
        res.append(result)
    else:
        temp = i[0] % i[1]
        result = i[1] - temp
        res.append(result)
print(*res, sep="\n")
