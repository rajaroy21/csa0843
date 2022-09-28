str=input('enter the word: ')
lower=0
upper=0
for i in  str:
    if(i.islower()):
        lower+=1
    else:
        upper+=1
    total=lower+upper
print("the number of lowercase characters is:", lower)
print("the number of uppercase characters is:", upper)
print("the total no of letters")
