esoda=float(input('Δώσε τα εσοδά σου:'))
foros=float(input('Δώσε το ποσό του φόρου που πλήρωσες:'))
if esoda>=10000:
    if foros<3000: 
        print('Κλέβει την εφορία')
    else:
        print('Eίναι νόμιμος')
else:
    if foros>5000:
        print('Yπερβολική φορολογία')
    else:
        print('Κανονική φορολογία')


