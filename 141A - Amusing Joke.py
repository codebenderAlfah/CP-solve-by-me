host = input()
guest = input()
mixed = input()
temp1 = []
temp2 = []
names = []
names[:0] = mixed
name1 = []
name1[:0] = host
name2 = []
name2[:0] = guest
for i in name1:
    if i in names:
        temp1.append(i)
        names.remove(i)
for j in name2:
    if j in names:
        temp2.append(j)
        names.remove(j)
if temp1 == name1 and temp2 == name2 and len(names) == 0:
    print("YES")
else:
    print("NO")
