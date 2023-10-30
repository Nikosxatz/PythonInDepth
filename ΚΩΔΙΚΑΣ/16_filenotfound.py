while True:
    try:
        filename=input('Δώσε όνομα αρχείου :')
        f=open(filename,'r')
    except FileNotFoundError:
        print('Λάθος όνομα αρχείου')
    else:
        pl=0
        sum=0
        for i in f:
            pl=pl+1
            ar=int(i)
            if pl==1:
                mn=ar
                mx=ar
            else:
                if ar>mx:
                    mx=ar
                elif ar<mn:
                    mn=ar
            sum=sum+ar
        f.close()
        mo=sum/pl
        print('Πλήθος=',pl,' Μέση τιμή=',mo)
        print('Μέγιστος=',mx,' Ελάχιστος=',mn)
        break
