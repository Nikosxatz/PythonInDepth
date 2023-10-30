mors=dict()
test_set={'.','-'}

# Εισαγωγή γραμμάτων
for p in range(65,91):
    while True:
        m=input('Δώσε κώδικα Μορς για το γράμμα '+chr(p)+'>')
        if set(m).issubset(test_set) and len(m)<=5:
            mors.update({chr(p):m})
            break
        else:
            print('Μη αποδεκτή ακολουθία Μορς')

# Εισαγωγή ψηφίων    
for p in range(48,57):
    while True:
        m=input('Δώσε κώδικα μορς για τo ψηφίο '+chr(p)+'>')
        if set(m).issubset(test_set) and len(m)<=5:
            mors.update({chr(p):m})
            break
        else:
            print('Μη αποδεκτή ακολουθία Μορς')

# Εισαγωγή φράσης για κωδικοποίηση        
frasi=input('Δώσε φράση για μετατροπή >')
if not frasi.isascii():
     print('Μη αποδεκτή φράση - επιτρέπονται μόνο λατινικοί χαρακτήρες και ψηφία')
frasi=frasi.upper()
lexeis=frasi.split()     
print(lexeis)
for lex in lexeis:
    for ch in lex:
        code=mors.get(ch)
        print(code,end='')
        print('  ',end='')
    print('       ',end='')
print('\n########### ΤΕΛΟΣ ###########')

