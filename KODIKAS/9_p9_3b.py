onomata=['Μαρία','Άννα','Χρύσα','Νίκος','Τάκης']
bathmoi=[[9,7,8.5],[6,9,3.5],[5,7.5,6.5],[3,5,2],[10,6,8.5]]
for i in range(len(bathmoi)):
    print(onomata[i],'=',max(bathmoi[i]))
onom=input('Δώσε όνομα : ')
if onomata.count(onom)>0:
    print('Οι βαθμοί του/της ',onom,' = ',bathmoi[onomata.index(onom)])
else:
    print('Δεν υπάρχει τέτοιο όνομα')
    



