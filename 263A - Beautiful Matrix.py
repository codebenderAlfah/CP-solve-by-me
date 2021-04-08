x = 0
y = 0
matrix = []
for i in range(5):
    arr = []
    arr = list(map(int, input().split()))
    matrix.append(arr)
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            x = i
            y = j
print(abs(abs(x-2)+abs(y-2)))
