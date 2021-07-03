prb = input()
ele = []
length = len(prb)
for i in range(length):
    if prb[i] !="+":
        temp = int(prb[i])
        ele.append(temp)
ele.sort()
print(*ele, sep = "+")
