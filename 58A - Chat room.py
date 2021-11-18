s = input()
count = 0
for i in s:
    if count == 0 and i == 'h':
        count += 1
    elif count == 1 and i == 'e':
        count += 1
    elif count == 2 and i == 'l':
        count += 1
    elif count == 3 and i == 'l':
        count += 1
    elif count == 4 and i == 'o':
        count += 1
if count == 5:
    print("YES")
else:
    print("NO")
