filename=input('Δώσε όνομα αρχείου > ')
pl=0
with open(filename,encoding='utf-8') as f:
    for line in f:
        if line=='':
            break
        pl=pl+1
        print(str(pl)+'.',line,end='')


    


    
