n = int(input())
trams = []
cap = 0
maxi = 0
for i in range(0, n):
    ele = list(map(int, input().split()))
    trams.append(ele)
for i in range(len(trams)):
    if i == 0:
        cap = trams[i][1]
    else:
        cap = (cap + trams[i][1]) - trams[i][0]
    if cap > maxi:
        maxi = cap
print(maxi)
