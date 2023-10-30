def elegxos_emveleias():
    def test_local():
        apot = 'Τοπική'

    def test_nonlocal():
        nonlocal apot
        apot = 'Οχι τοπική'

    def test_global():
        global apot
        apot = 'Καθολική'

    apot = 'Αρχική'
    test_local()
    print('Μετά από test_local:', apot)
    test_nonlocal()
    print('Μετα από test_nonlocal:', apot)
    test_global()
    print('Μετά από test_global:', apot)

# Κυρίως πρόγραμμα
apot='test'
elegxos_emveleias()
print('Στη καθολική εμβέλεια:', apot)























