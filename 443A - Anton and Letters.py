anton = list(input().split(', '))
total = []
uniq = []
for i in range(0, len(anton)):
    if len(anton) == 1:
        x = anton[i]
        if len(x) > 2:
            x = anton[i][1]
            total.append(x)
        else:
            break
    elif i == 0:
        x = anton[i][1]
        total.append(x)
    elif i == len(anton)-1:
        x = anton[i][0]
        total.append(x)
    else:
        x = anton[i]
        total.append(x)
for i in total:
    if i not in uniq:
        uniq.append(i)
print(len(uniq))
