onomata=['Μαρία','Άννα','Χρύσα','Νίκος','Τάκης']
bathmoi=[[9,7,8.5],[6,9,3.5],[5,7.5,6.5],[3,5,2],[10,6,8.5]]
for i in range(len(bathmoi)):
    print(onomata[i],'=',max(bathmoi[i]))
onom=input('Δώσε όνομα : ')
vrika=False
for i in range(len(onomata)):
    if onom==onomata[i]:
        print('Οι βαθμοί του ',onom,' = ',bathmoi[i])
        vrika=True
        break
if not vrika:
    print('Δεν υπάρχει τέτοιο όνομα')
    



