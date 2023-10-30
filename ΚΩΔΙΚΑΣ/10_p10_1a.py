def is_password_ok(paswd):
    ok=True
    mes=''
    if (len(paswd)<8):
        ok=False
        mes=mes+'Είναι μικρότερος από 8 χαρακτήρες\n'
    if paswd.islower() or paswd.isupper():
        ok=False
        mes=mes+'Πρέπει να υπάρχουν πεζοι και κεφαλαιοι χαρακτήρες\n'
    if paswd.find(' ')!=-1:
        ok=False
        mes=mes+'Δεν επιτρέπονται κενά\n'
    if not paswd.isascii():
        ok=False
        mes=mes+'Δεν επιτρέπονται ελληνικά\n'     
    special_char=False
    for i in '%$@#!':
        if paswd.find(i)!=-1:
            special_char=True
            break
    if special_char==False:
        ok=False
        mes=mes+'Δεν υπάρχει κανένας ειδικός χαρακτήρας\n'
        
    return (ok,mes)

# Κυρίως πρόγραμμα
plist=['hDfgs!d','rgag23@@','123 4!!Kl','123 Νίκος','TeleioP@sw0rd']
for p in plist:
    res=is_password_ok(p)
    if res[0]:
        print('Αποδεκτός κωδικός:',p)
    else:
        print('Μη αποδεκτός κωδικός:',p,' διότι ...')
        print(res[1])
 

