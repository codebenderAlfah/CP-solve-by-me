n = int(input())
dom = []
count = 1
for i in range(0, n):
    ele = input()
    dom.append(ele)
for i in range(0, len(dom)-1):
    if dom[i] == dom[i+1]:
        count += 0
    else:
        count += 1
print(count)
