import random
def suffle(Lst):
    for i in range(len(Lst)):
        p1=random.randint(0,len(Lst)-1)
        p2=random.randint(0,len(Lst)-1)
        Lst[p1],Lst[p2]=Lst[p2],Lst[p1]
        
filename=input('Δώσε όνομα αρχείου >')
f=open(filename,'r',encoding='greek')
fout=open('code','wb')
list1=[]
list2=[]
pos=3
while True:
    ch=f.read(1)
    if ch=='':
        break
    list1.append(ch)
    list2.append(pos)
    pos=pos+3
f.close()
suffle(list2)

for i in range(len(list2)):
    fout.seek(list2[i])
    fout.write(bytes(list1[i],encoding='greek'))
    if i==len(list2)-1:
        pos=(0).to_bytes(2,'little')
    else:
        pos=(list2[i+1]).to_bytes(2,'little')
    fout.write(pos)
print('Αρχική θέση :',list2[0])
fout.close()
