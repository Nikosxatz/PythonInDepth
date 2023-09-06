for i in range(10):
    onoma=input('Δώσε όνομα:')
    ypsos=float(input('Δώσε ύψος:'))
    if i==0:
        max=ypsos
        min=ypsos
        max_onom=onoma
        min_onom=onoma
    elif ypsos>max:
        max=ypsos
        max_onom=onoma   
    elif ypsos<min:
        min=ypsos
        min_onom=onoma
print('Ψηλότερος:',max_onom,' Κοντύτερος:',min_onom)
    
        
    
