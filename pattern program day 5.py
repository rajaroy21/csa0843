ch= input(" Enter the Character to be printed  : ")
rows=0
rows = int(input("Max number of time printed : "))
if rows<=0:
    print("please enter the positive number")
for i in range(1, rows+1):
    for j in range(1, i+1):
        print('%c' %ch, end = '')
    print()
