A=[]
B=[]
c=[]
d=[]
n=int(input("Enter the n value,it is nxn matrix\n:"))
print("enter matrix 1")
for i in range(0,n):
    row=[]
    for j in range(0,n):
        row.append(int(input()))
    A.append(row)

print("enter matrix 2")
for i in range(0,n):
    row=[]
    for j in range(0,n):
        row.append(int(input()))
    B.append(row)
print("1st matrix")
print(A)
print("2nd matrix")
print(B)
for i in range(0,n):
    c=[]
    for j in range(0,n):
        c.append(A[i][j]+B[i][j])
    d.append(c)
print("addition of two matrix")    
print(d)
