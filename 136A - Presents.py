n = int(input())
f = [0]*n
g = [0]*n
f = list(map(int, input().split()))
for i in range(n):
    x = f[i]
    g[x-1] = i + 1
print(*g)
