h=int(input('Δώσε ημέρα:'))
m=int(input('Δώσε μήνα:'))
if (h>=21 and m==3) or (h<=20 and m==4):
    print('Κριος')
elif (h>=21 and m==4) or (h<=20 and m==5):
    print('Ταύρος')
elif (h>=21 and m==5) or (h<=21 and m==6):
    print('Δίδυμοι')
elif (h>=22 and m==6) or (h<=22 and m==7):
    print('Καρκίνος')
elif (h>=23 and m==7) or (h<=22 and m==8):
    print('Λέων')
elif (h>=23 and m==8) or (h<=22 and m==9):
    print('Παρθένος')
elif (h>=23 and m==9) or (h<=23 and m==10):
    print('Ζυγός')
elif (h>=24 and m==10) or (h<=22 and m==11):
    print('Σκορπιός')
elif (h>=23 and m==11) or (h<=21 and m==12):
    print('Τοξότης')
elif (h>=22 and m==12) or (h<=20 and m==1):
    print('Αιγόκερως')
elif (h>=21 and m==1) or (h<=19 and m==2):
    print('Υδροχόος')
elif (h>=20 and m==2) or (h<=20 and m==3):
    print('Ιχθύς')
else:
    print('Λάθος ημερομηνία!!!')

	














