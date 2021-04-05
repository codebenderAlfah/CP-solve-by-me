n = int(input())
solves = []
y = 0
for i in range(0, n):
    ele = input()
    solves.append(ele)
# print(solves)
for solve in solves:
    x = 0
    for i in range(0, len(solve)):
        if solve[i] == '1':
            x = x+1
    if x >= 2:
        y = y+1
print(y)
