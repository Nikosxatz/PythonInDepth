class LathosEmail(Exception):
    pass
class LigoiXaraktires(LathosEmail):
    pass
class OxiEllinika(LathosEmail):
    pass
class OxiKena(LathosEmail):
    pass
class OxiPapaki(LathosEmail):
    pass

while True:
    try:
        email=input('Δώσε το email σου:')
        if email.count('@')!=1:
            raise OxiPapaki('Δεν υπάρχει @')
        elif (len(email)<5):
            raise LigoiXaraktires('Έχει πολύ λίγους χαρακτήρες')
        elif email.find(' ')!=-1:
            raise OxiKena('Δεν επιτρέπονται κενά')
        elif not email.isascii():
            raise OxiEllinika('Δεν επιτρέπονται ελληνικά')
    except LigoiXaraktires as e1:
        print(e1,'- Δώσε άλλo email')
    except OxiKena as e2:
        print(e2,'- Δώσε άλλo email')  
    except OxiEllinika as e3:
        print(e3,'- Δώσε άλλo email')  
    except OxiPapaki as e4:
        print(e4,'- Δώσε άλλo email')  
    else:
        break
print('Αποδεκτό !!!')  



 

