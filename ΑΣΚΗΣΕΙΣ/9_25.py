onomata=[]
o=input('Δώσε όνομα : ')
onomata.append(o)
thesi=0
for i in range(1,10):
    o=input('Δώσε όνομα : ')
    j=0
    while o>onomata[j]:
        j=j+1
        if j==len(onomata):
            break
    onomata.insert(j,o)

print(onomata)

    



