def convert_list(Lst):
	tt=str.maketrans('ΆΈΉΊΌΎΏάέήίόύώ','ΑΕΗΙΟΥΩαεηιουω','1234567890 _')
	for i in range(len(Lst)):
		Lst[i]=Lst[i].lower()
		Lst[i]=Lst[i].capitalize()
		Lst[i]=Lst[i].translate(tt)
		if Lst[i].rfind('σ')==len(Lst[i])-1:
			Lst[i]=Lst[i][:-1]+'ς'
# Κυρίως πρόγραμμα
L1=['ΝίΚΟΣ','τάκησ','γιώργος','Άγγελος','στρατήσ']
convert_list(L1)
print(L1)
L2=['mARY','Άννα56','γιώργος','Ίωνασ_22 ','σΤΡΑ   ΤΗΣ']
convert_list(L2)
print(L2)

