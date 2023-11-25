Lst3=[['Μαρία',6,7,8.5],['Νίκος',3,6,9],['Αννα',5,7.5,6.5],['Τάκης',3,5,2]]
for i in range(len(Lst3)):
    s=0
    for j in range(1,len(Lst3[i])):
        s=s+Lst3[i][j]
    mo=s/(len(Lst3[i])-1)
    print(Lst3[i][0],'=',mo)
    



