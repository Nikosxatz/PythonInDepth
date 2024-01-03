filename=input('Δώσε όνομα αρχείου > ')
with open(filename,'r',encoding='utf-8') as f:
    for line in f:
        if line.endswith('\n'):
            m=len(line)-1
        else:
            m=len(line)
        print(m)

