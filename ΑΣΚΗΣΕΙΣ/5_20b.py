# Άλλη λύση της άσκησης 5.20 με χρήση λιστών, του τελεστή in και της μεθόδου index

h=int(input('Δώσε ημέρα:'))
m=int(input('Δώσε μήνα:'))
# Η λίστα list_dates περιέχει λογικές εκφράσεις από τις οποίς μόνο μια θα είναι True
list_dates=[
    h>=21 and m==3  or h<=20 and m==4,
    h>=21 and m==4  or h<=20 and m==5, 
    h>=21 and m==5  or h<=21 and m==6,
    h>=22 and m==6  or h<=22 and m==7,
    h>=23 and m==7  or h<=22 and m==8,
    h>=23 and m==8  or h<=22 and m==9,
    h>=23 and m==9  or h<=23 and m==10,
    h>=24 and m==10 or h<=22 and m==11,
    h>=23 and m==11 or h<=21 and m==12,
    h>=22 and m==12 or h<=20 and m==1,
    h>=21 and m==1  or h<=19 and m==2,
    h>=20 and m==2  or h<=20 and m==3
    ]
list_zodiacs=['Κριος','Ταύρος','Δίδυμοι','Καρκίνος','Λέων','Παρθένος','Ζυγός','Σκορπιός','Τοξότης','Αιγόκερως','Υδροχόος','Ιχθύς']

if True  in list_dates:    
    number=list_dates.index(True)
    print (list_zodiacs[number])
else:
    print('Λάθος ημερομηνία!!!')
