n = int(input())
stats = []
x = 0
for i in range(0, n):
    ele = input()
    stats.append(ele)
for stat in stats:
    if stat[0] == "+" or stat[2] == "+":
        x = x+1
    elif stat[0] == "-" or stat[2] == "-":
        x = x-1
print(x)
