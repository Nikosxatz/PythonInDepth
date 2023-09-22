def convert_list(l):
    tt=str.maketrans('ΆΈΉΊΌΎΏάέήίόύώ','ΑΕΗΙΟΥΩαεηιουω','1234567890 _')
    for i in range(len(l)):
        l[i]=l[i].lower()
        l[i]=l[i].capitalize()
        l[i]=l[i].translate(tt)
        if l[i].rfind('σ')==len(l[i])-1:
            l[i]=l[i][:-1]+'ς'

# Κυρίως πρόγραμμα
l1=['ΝίΚΟΣ','τάκησ','γιώργος','Άγγελος','στρατήσ']
convert_list(l1)
print(l1)
l2=['mARY','Άννα56','γιώργος','Ίωνασ_22 ','σΤΡΑ   ΤΗΣ']
convert_list(l2)
print(l2)
