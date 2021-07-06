a = input()
b = input()
sum = []
ele = 0
for i in range(len(a)):
    if a[i] == b[i]:
        ele = '0'
    else:
        ele = '1'
    sum.append(ele)
print("".join(sum))
