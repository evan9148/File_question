file_data = open("question3.txt","r")
file_line = file_data.read()
# file_line = file_line.split("/n")
print(file_line)
a=[]
for i in file_line:
    value=i.strip(",",2)
    a.append(value)
output=[]
for j in (a):
    b=[]
    for c in j:
        b.append(c)
    output.append(b)
print(output)
    
# i=0
# a=[]
# while i<len(file_line):
#     a.append(file_line)
#     break
#     j=0
# b=[]
# while j<len(a):
#     b.append(a[j])
#     break
#     j=j+1
#     i=i+1
# print(b)