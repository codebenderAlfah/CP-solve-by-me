n = int(input())
rocks = input()
count = 0
for i in range(n-1):
    if rocks[i] == rocks[i+1]:
        count = count+1
print(count)
