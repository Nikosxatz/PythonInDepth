with open('bin_out','wb') as fout:
    while True:
        onoma=input('Δώσε όνομα > ')
        if onoma=='':
            break
        fout.write(onoma.encode('utf-8'))
        fout.write(b'\xff')


