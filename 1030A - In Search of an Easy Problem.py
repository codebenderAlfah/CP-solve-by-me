n = int(input())
s = input()
count = 0
for i in s:
    if i == '0':
        count = count + 1
if count == n:
    print("EASY")
else:
    print("HARD")
