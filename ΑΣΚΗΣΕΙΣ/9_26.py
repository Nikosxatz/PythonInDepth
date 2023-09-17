def paremvoli(o,b):
    for i in range(len(o)):
        b[i].insert(0,o[i])

# Κυρίως πρόγραμμα        
onomata=['Νικος','Τάκης','Χρύσα','Άννα','Μαρία']
bathmoi=[[5,6,3],[8,9,9],[3.5,6,7],[6,7],[5,6.5,7,6]]
paremvoli(onomata,bathmoi)
print(bathmoi)

