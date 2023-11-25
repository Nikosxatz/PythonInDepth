def display():
    ''' Εσωτερικές συναρτήσεις '''
    def test1():
        a=20
    def test2():
        nonlocal a
        a=10       
    def test3():
        global a
        a=5
    a=30
    test1()
    print(a)
    test2()
    print(a)
    test3()
    print(a)

# Κυρίως πρόγραμμα
a=40
display()
print(a)


        
