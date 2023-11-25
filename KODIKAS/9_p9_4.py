def mysort(Lst):
    n=len(Lst)
    for i in range(1,n):
        for k in range(n-1,i,-1):
            if Lst[k]<Lst[k-1]:
                temp=Lst[k]
                Lst[k]=Lst[k-1]
                Lst[k-1]=temp

bathmoi=[['Μαρία',9,7,8.5],['Νίκος',6,9,3.5],['Αννα',5,7.5,6.5],['Τάκης',3,5,2]]
for i in bathmoi:
    mysort(i)
print(bathmoi)
    



