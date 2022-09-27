s=str(input("s :"))
t=str(input("t :"))
g=[]
h=[]
for i in s:
    if i not in g:
        g.append(s.index(i))
for j in t:
    if j not in h:
        h.append(t.index(j))
if g==h:
    print("true")
else:
    print("flase")
