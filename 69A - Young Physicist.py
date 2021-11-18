n = int(input())
x = []
y = []
z = []
for i in range(n):
    xi, yi, zi = map(int, input().split())
    x.append(xi)
    y.append(yi)
    z.append(zi)
x1 , y1, z1 = sum(x), sum(y), sum(z)
if x1 == 0 and y1 == 0 and z1 == 0:
    print("YES")
else:
    print("NO")
