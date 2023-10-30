def is_password_ok(paswd):
    
    listmsg=['Είναι μικρότερος από 8 χαρακτήρες',
             'Πρέπει να υπάρχουν πεζοι και κεφαλαιοι χαρακτήρες',
             'Δεν επιτρέπονται κενά',
             'Δεν επιτρέπονται ελληνικά',
             'Δεν υπάρχει κανένας ειδικός χαρακτήρας']
    
    special_set=set('%$@#!')    
    paswd_set=set(paswd)

    listok=[not len(paswd)<8,
           not paswd.islower() and not paswd.isupper(),
           paswd.find(' ')==-1,
           paswd.isascii(),
           not special_set.isdisjoint(paswd_set)]     

    listerror=[listmsg[i] for i in range(len(listmsg)) if listok[i]==False ]       
  
    return listerror

# Κυρίως πρόγραμμα
plist=['hDfgxxs!d','rgag23@@','123 4!!Kl','123 Νίκος','TeleioP@sw0rd']
for p in plist:
    if not is_password_ok(p):
        print('Το',p,'είναι τέλειο password')
    else:
        print(p,is_password_ok(p))




