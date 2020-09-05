list1=["delhi","delhi","shimla","other","shimla"]
i=0
a=[]
b=[]
c=[]
while i<len(list1):
    if list1[i]=="delhi":
        a.append(list1[i])
    elif list1[i]=="other":
        b.append(list1[i])
    else:
        c.append(list1[i])
    i=i+1
print(a)
print(b)
print(c)