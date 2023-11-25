Filoi=['Νίκος','Βασίλης','Μαρία','Λευτέρης']
Onoma=input('Δώσε το όνομά σου:')
if Onoma not in Filoi:
    Filoi.append(Onoma)
    print('Το όνομά σου προστέθηκε στους φίλους μου')
else: 
    print('Είσαι ήδη στη λίστα των φίλων μου')
print(Filoi)









