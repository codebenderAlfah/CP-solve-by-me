n, t = input().split()
n = int(n)
t = int(t)
line = input()
for i in range(t):
    line = line.replace("BG", "GB")
print(line)
