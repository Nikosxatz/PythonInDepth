import math

class trionymo:
    def __init__(self,s1,s2,s3):
        self.__a=s1
        self.__b=s2
        self.__c=s3
        
    def syntelestes(self,s1,s2,s3):
        self.__a=s1
        self.__b=s2
        self.__c=s3
        
    def __diakrinousa(self):
        d=self.__b**2-4*self.__a*self.__c
        return d

    def exei_pragmatikes_rizes(self):
        if self.__diakrinousa()>=0:
            return True
        else:
            return False

    def rizes(self):
        if self.__diakrinousa()>=0:
            r1=(-self.__b+math.sqrt(self.__diakrinousa()))/(2*self.__a)
            r2=(-self.__b-math.sqrt(self.__diakrinousa()))/(2*self.__a)    
            return (r1,r2)
        else:
            return None

# Κυρίως πρόγραμμα
ex1=trionymo(1,2,-3)
# Έλεγχος για πραγματικές ρίζες και εμφάνιση ριζών
if ex1.exei_pragmatikes_rizes():
    t=ex1.rizes()
    print('r1=',t[0],' r2=',t[1])
else:
    print('Δεν έχει πραγματικές ρίζες')    
while True:
    sn1=float(input('Δώσε πρώτο συντελεστή:'))
    sn2=float(input('Δώσε δεύτερο συντελεστή:'))
    sn3=float(input('Δώσε τρίτο συντελεστή:'))
    # Διακοπή επαναληπτικής λειτουργίας στην περίπτωση συντελεστή με τιμή 0
    if sn1==0 or sn2==0 or sn3==0:
        break
    # Αλλαγή συντελεστών εξίσωσης
    ex1.syntelestes(sn1,sn2,sn3)
    # Έλεγχος για πραγματικές ρίζες και εμφάνιση ριζών
    if ex1.exei_pragmatikes_rizes():
        print('r1=',t[0],' r2=',t[1])
    else:
        print('Δεν έχει πραγματικές ρίζες')


