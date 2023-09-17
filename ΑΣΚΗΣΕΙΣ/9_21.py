def dikaioyxoi(a,n):
    for i in n:
        if i in a:
            a.pop(a.index(i))

# Κυρίως πρόγραμμα
all=['Μαρία','Μιχαήλ','Πάτροκλος','Άννα','Χρύσα','Τάκης']
oxi=['Μαρία','Άννα','Τάκης']
dikaioyxoi(all,oxi)
print(all)
