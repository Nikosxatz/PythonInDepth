filename=input('Δώσε όνομα αρχείου > ')
pl=0
with open(filename,'r',encoding='utf-8') as f:
    for line in f:
        if line=='':
            break
        list_line=line.split()
        pl=pl+len(list_line)
print('Το αρχειο έχει',pl,'λέξεις')

    


    
