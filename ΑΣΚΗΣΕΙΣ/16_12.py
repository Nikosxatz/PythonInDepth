email=input('Δώσε το email σου:')
if email.count('@')!=1:
    print('Δεν υπάρχει @')
elif len(email)<5:
    print('Έχει πολύ λίγους χαρακτήρες')
elif email.find(' ')!=-1:
    print('Δεν επιτρέπονται κενά')
elif not email.isascii():
    print('Δεν επιτρέπονται Ελληνικά')
else:
    print('Αποδεκτό !!!')
 



 

