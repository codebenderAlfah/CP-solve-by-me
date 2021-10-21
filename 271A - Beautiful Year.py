n = int(input()) #input
flag = False
while flag == False:
    n += 1
    temp = n  # starting with next year
    a = temp % 10   #1st digit
    temp = int(temp/10)
    b = temp % 10   #2nd digit
    temp = int(temp/10)
    c = temp % 10   #3rd digit
    temp = int(temp/10)
    d = temp % 10 #4th digit
    if a != b and a != c and a != d and b != c and b != d and c != d: #checking
        flag = True
print(n)
