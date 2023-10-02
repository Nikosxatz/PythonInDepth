filename=input('Δώσε όνομα αρχείου > ')
frasi=input('Δώσε φράση > ')
pl=0
brika=False
with open(filename,'r',encoding='utf-8') as f:
    for line in f:
        if line=='':
            break
        pl=pl+1
        if frasi in line:
            print(str(pl)+'.',line,end='')
            brika=True
if not brika:
    print('Δεν βρέθηκε καμία γραμμή να περιέχει αυτή τη φράση!')

    


    
