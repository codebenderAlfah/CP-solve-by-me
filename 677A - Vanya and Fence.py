n, h = input().split() #friends and wall height
n = int(n)
h = int(h)
f = []
f = list(map(int,input(). split())) #friends heights
count = 0
for j in f:
    if j <= h:
        count += 1
    elif j > h:
        count += 2
print(count)

