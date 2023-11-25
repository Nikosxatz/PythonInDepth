sum=pl=0
while True:
    try:
        il = int(input('Δώσε ηλικία > '))
    except ValueError:
        print('Εππ ... δώσε σωστό ακέραιο αριθμό!')
    except KeyboardInterrupt:
        print('Κάτω τα χεράκια ...')
    else:
        if il<=0:
            break
        sum=sum+il
        pl=pl+1
try:
    mo=sum/pl
except ZeroDivisionError:  
    print('Μάλλον δεν έδωσες καμία ηλικία')
else:
    print('Μέσος όρος ηλικιών =',mo)
