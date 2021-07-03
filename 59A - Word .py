word = input()
count = 0
length = len(word)
for i in range(length):
    if word[i].isupper():
        count = count + 1
if count > length/2:
    print(word.upper())
else:
    print(word.lower())
