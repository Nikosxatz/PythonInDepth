class oxima:
    def info1(self):
        print('Είμαι ένα όχημα – μπορώ να σε μεταφέρω')
    
class car(oxima):
    def info2(self):
        print('Είμαι ένα αυτοκίνητο')  

# Κυρίως πρόγραμμα
c1=car()
c1.info1()
c1.info2()




