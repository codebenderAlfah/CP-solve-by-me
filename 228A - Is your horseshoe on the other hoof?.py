shoes = list(map(int, input(). split())) #takin input
uniq = []
for i in shoes:
    if i not in uniq:
        uniq.append(i) #checking for same color shoe
print(4-len(uniq)) #need to buy
