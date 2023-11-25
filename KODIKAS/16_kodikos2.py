class LathosKodikos(Exception):
    def __init__(self,kd):
        self.kodikos=kd

class LigoiXaraktires(LathosKodikos):
    def __str__(self):
        return 'Ο κωδικός '+self.kodikos+' έχει λιγότερους από 8 χαρακτήρες'

class PezoiKefalaioi(LathosKodikos):
    def __str__(self):
        return 'Ο κωδικός '+self.kodikos+' πρέπει να διαθέτει πεζούς και κεφαλαίους χαρακτήρες'

class OxiEllinika(LathosKodikos):
    def __str__(self):
        return 'Ο κωδικός '+self.kodikos+' δεν πρέπει να διαθέτει ελληνικούς χαρακτήρες'

class OxiKena(LathosKodikos):
    def __str__(self):
        return 'Ο κωδικός '+self.kodikos+' δεν πρέπει να διαθέτει κενά'

class OxiEidikos(LathosKodikos):
    def __str__(self):
        return 'Ο κωδικός '+self.kodikos+' πρέπει να διαθέτει κάποιον ειδικό χαρακτήρα'

# Κυρίως πρόγραμμα
while True:
    try:
        passwd=input('Δώσε κωδικό:')
        if (len(passwd)<8):
            raise LigoiXaraktires(passwd)
        if passwd.islower() or passwd.isupper():
            raise PezoiKefalaioi(passwd)
        if passwd.find(' ')!=-1:
            raise OxiKena(passwd)
        if not passwd.isascii():
            raise OxiEllinika(passwd)     
        special_char=False
        for i in '%$@#!':
            if passwd.find(i)!=-1:
                special_char=True
                break
        if special_char==False:
               raise OxiEidikos(passwd)
    except LigoiXaraktires as e1:
        print(e1,'- Δώσε άλλον κωδικό')                  
    except PezoiKefalaioi as e2:
        print(e2,'- Δώσε άλλον κωδικό')  
    except OxiKena as e3:
        print(e3,'- Δώσε άλλον κωδικό')  
    except OxiEllinika as e4:
        print(e4,'- Δώσε άλλον κωδικό')  
    except OxiEidikos as e5:
        print(e5,'- Δώσε άλλον κωδικό')  
    else:
        break
print('Σωστός !!!')
 

