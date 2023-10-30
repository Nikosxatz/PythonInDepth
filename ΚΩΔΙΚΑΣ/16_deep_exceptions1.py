class LathosKodikos(Exception):
    pass

class LigoiXaraktires(LathosKodikos):
    pass

class OxiKena(LathosKodikos):
    pass

class PezoiKefalaioi(LathosKodikos):
    pass

def get_passwd():
    while True:
        passwd=input('Δώσε κωδικό:')
        try:
            if (len(passwd)<8):
                raise LigoiXaraktires('Είναι μικρότερος από 8 χαρακτήρες')
            if passwd.islower() or passwd.isupper():
                raise PezoiKefalaioi('Πρέπει να υπάρχουν πεζοί και κεφαλαίοι χαρακτήρες')
            if passwd.find(' ')!=-1:
                raise OxiKena('Δεν επιτρέπονται κενά')
        except LigoiXaraktires as e1:
            print(e1,'- Δώσε άλλον κωδικό ΣΥΝ')
        else:
            break
 
# Κυρίως πρόγραμμα
while True:
    try:
        get_passwd()
    except LigoiXaraktires as e1:
        print(e1,'- Δώσε άλλον κωδικό ΚΠ')                  
    except PezoiKefalaioi as e2:
        print(e2,'- Δώσε άλλον κωδικό KΠ')  
    except LathosKodikos as e3:
        print(e3,'- Δώσε άλλον κωδικό ΚΠ')  
    else:
        break
print('Σωστός !!!')
 

