def display():
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
    print('μετά από test1',a)
    test2()
    print('μετά από test2',a)
    test3()
    print('μετά από test3',a)
    

# Κυρίως πρόγραμμα
a=40
display()
print('μετά από display',a)























