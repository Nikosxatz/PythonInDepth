fraseis=[]
while True:
    try:
        s=input('Γράψε κάτι > ')
        if s=='':
            break
        else:
            fraseis.append(s)
    except KeyboardInterrupt:
        print('Επ... κάτω τα χέρια από το πληκτρολόγιο!')
    except MemoryError:
        break
for f in fraseis:
    print(f)
