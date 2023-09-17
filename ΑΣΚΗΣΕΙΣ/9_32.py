def commons(Lst1,Lst2):
    yparxei=False
    for i in range(len(Lst1)):
        if Lst1[i] in Lst1[:i-1]:
            continue
        for j in Lst2:
            if Lst1[i]==j:
                print(j)
                yparxei=True
                break
    if not yparxei:
        print('Οι λίστες δεν έχουν κανένα κοινό στοιχείο')

# Κυρίως πρόγραμμα           
a=['Νικος','Τάκης','Χρύσα','Άννα','Μαρία','Τάκης']
b=['Μιχαήλ','Φωτεινή','Τάκης','Σπύρος','Χρύσα','Μάνος','Μαρία','Τάκης']
commons(a,b)

