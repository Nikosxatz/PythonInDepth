ilikia=int(input('Δώσε την ηλικία σου:'))
if ilikia<=12:
    print('Είσαι παιδί')
elif ilikia<=18:
    print('Είσαι έφηβος')
elif ilikia<=40:
    if ilikia<=30:
        print('Είσαι νέος')
    else:
        print('Είσαι ώριμος')
else: 
    print('Είσαι μεσήλικας')






