def display(a,b):
    if type(a) is str and type(b) is int:
        for i in range(b):
            print(a,end=' ')
        print()
    elif type(a) is int and type(b) is str:
        for i in range(a):
            print(b)
    elif type(a) is int and type(b) is int:
        for i in range(a,b+1):
            print(i)
    elif type(a) is str and type(b) is str:
        print(a+' '+b)
    else:
        print('Λάθος κλήση!')
# Κυρίως πρόγραμμα
display(5,7)
display('Python',3)
display(2,'σε βάθος')
display('Python','σε βάθος')























