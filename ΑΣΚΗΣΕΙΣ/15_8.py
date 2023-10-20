class oxima:
    def info(self):
        print('Είμαι ένα όχημα – μπορώ να σε μεταφέρω')
    
class car(oxima):
    def info(self):
        super().info()
        print('Είμαι ένα αυτοκίνητο')  

# Κυρίως πρόγραμμα
c1=car()
c1.info()





