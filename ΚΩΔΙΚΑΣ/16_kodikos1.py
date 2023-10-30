class LathosKodikos(Exception):
    pass

class LigoiXaraktires(LathosKodikos):
    pass

class PezoiKefalaioi(LathosKodikos):
    pass

class OxiEllinika(LathosKodikos):
    pass

class OxiKena(LathosKodikos):
    pass

class OxiEidikos(LathosKodikos):
    pass


# Κυρίως πρόγραμμα
while True:
    try:
        passwd=input('Δώσε κωδικό:')
        if (len(passwd)<8):
            raise LigoiXaraktires('Είναι μικρότερος από 8 χαρακτήρες')
        if passwd.islower() or passwd.isupper():
            raise PezoiKefalaioi('Πρέπει να υπάρχουν πεζοι και κεφαλαίοι χαρακτήρες')
        if passwd.find(' ')!=-1:
            raise OxiKena('Δεν επιτρέπονται κενά')
        if not passwd.isascii():
            raise OxiEllinika('Δεν επιτρέπονται ελληνικά')     
        special_char=False
        for i in '%$@#!':
            if passwd.find(i)!=-1:
                special_char=True
                break
        if special_char==False:
               raise OxiEidikos('Δεν υπάρχει κανένας ειδικός χαρακτήρας')
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
 

