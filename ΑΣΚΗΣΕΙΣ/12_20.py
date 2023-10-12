import random

class test:
    def __init__(self):
        self.ar=random.randint(1,1000)
        print('Δημιουργήθηκε το',self.ar)
    def __del__(self):
        print('Καταστράφηκε το',self.ar)    

# Κυρίως πρόγραμμα
t1=test()
del t1
