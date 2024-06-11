c = input()
b = c.split( )
c = 0
target = int(input())
for i in range(len(b)):
    c = c+int(b[i])
print(c)

for i in range(len(b)):
    for j in range(i,len(b)):
        if int(b[i])+int(b[j]) == target:
            print(b[i],b[j])