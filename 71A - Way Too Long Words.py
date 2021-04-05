n = int(input())
words = []
for i in range(0, n):
    ele = input()
    words.append(ele)
for word in words:
    if len(word)>10:
        x=word[0]+str((len(word)-2))+word[len(word)-1]
    else:
        x=word
    print(x)
