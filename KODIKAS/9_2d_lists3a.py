Lst2=[[6,7,8.5,10],[3,6],[5,7.5,6.5],[3]]
for i in range(len(Lst2)):
    s=0
    for j in range(len(Lst2[i])):
        s=s+Lst2[i][j]
    mo=s/len(Lst2[i])
    print('Μέσος όρος',i+1,'=',mo)
    



