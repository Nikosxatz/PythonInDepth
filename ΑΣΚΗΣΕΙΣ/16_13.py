class LathosEmail(Exception):
    pass
class LigoiXaraktires(LathosEmail):
    def __init__(self,mail):
        self.m=mail
    def __str__(self):
        return 'Η διεύθυνση '+self.m+' έχει πολύ λίγους χαρακτήρες'    
class OxiEllinika(LathosEmail):
    def __init__(self,mail):
        self.m=mail
    def __str__(self):
        return 'Η διεύθυνση '+self.m+' περιέχει ελληνικά'
class OxiKena(LathosEmail):
    def __init__(self,mail):
        self.m=mail
    def __str__(self):
        return 'Η διεύθυνση '+self.m+' περιέχει κενά'
class OxiPapaki(LathosEmail):
    def __init__(self,mail):
        self.m=mail
    def __str__(self):
        return 'Η διεύθυνση '+self.m+' δεν έχει @'

while True:
    try:
        email=input('Δώσε το email σου:')
        if email.count('@')!=1:
            raise OxiPapaki(email)
        elif (len(email)<5):
            raise LigoiXaraktires(email)
        elif email.find(' ')!=-1:
            raise OxiKena(email)
        elif not email.isascii():
            raise OxiEllinika(email)
    except LigoiXaraktires as e1:
        print(e1)
    except OxiKena as e2:
        print(e2)  
    except OxiEllinika as e3:
        print(e3)  
    except OxiPapaki as e4:
        print(e4)  
    else:
        break
print('Αποδεκτό !!!')  



 

