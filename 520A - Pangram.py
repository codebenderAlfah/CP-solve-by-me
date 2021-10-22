n = int(input())
word = input()
word = word.lower()
pang = []
if len(word) < 26:
    print('NO')
else:
    for i in range(0, len(word)):
        if word[i] not in pang:
            pang.append(word[i])
    if len(pang) == 26:
        print('YES')
    else:
        print('NO')
