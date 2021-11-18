x = input()
x = x.lower()
vow = ['a', 'e', 'i', 'o', 'u']
sol = ""
for i in x:
    if i not in vow:
        sol += '.'
        sol += i
print(sol)
