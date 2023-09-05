ypsos=float(input('Δώσε το ύψος σου:'))
baros=float(input('Δώσε το βάρος σου:'))
dms=baros/(ypsos*ypsos)
if dms<18.5:
    print('Λιποβαρής')
elif dms<25:
    print('Κανονικός')
elif dms<30:
    print('Υπέρβαρος')   
else:
    print('Παχύσαρκος')  











