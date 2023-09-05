def display():
    ''' Εσωτερικές συναρτήσεις '''
    a=50
    def test1():
        a=20
        print(a)
    def test2():
        print(a)
    def test3():
        nonlocal a
        a=5
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


        
