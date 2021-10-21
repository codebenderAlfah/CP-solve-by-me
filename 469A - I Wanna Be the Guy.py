lavels = int(input())
x = list(map(int, input(). split()))
y = list(map(int, input(). split()))
uniq = []
for i in range(1, len(x)):
    if x[i] not in uniq and x[i] != 0:
        uniq.append(x[i])
for i in range(1, len(y)):
    if y[i] not in uniq and y[i] !=0:
        uniq.append(y[i])
if len(uniq) == lavels:
    print( "I become the guy.")
else:
    print("Oh, my keyboard!")
