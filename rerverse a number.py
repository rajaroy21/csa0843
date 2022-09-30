try:
    n=int(input("enter the number:"))
    l=str(n)
    h=l[::-1]
    print(h)
except ValueError:
    print("enter the numbers only")
