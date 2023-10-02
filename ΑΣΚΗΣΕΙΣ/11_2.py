filename=input('Δώσε όνομα αρχείου > ')
f=open(filename,'r',encoding='utf-8')
pl=0
while True:
    ch=f.read(1)
    if ch=='':
        break
    if ch==' ':
        pl=pl+1
f.close()
print('Πλήθος:',pl)

    


    
