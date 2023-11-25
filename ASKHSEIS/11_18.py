fm=open('morse.txt','r',encoding='cp1253')
morse=dict()
for m in fm:
    line=m.split()
    morse.update({line[1]:line[0]})         # Δημιουργεί λεξικό με κλειδί τον κωδικό Μορσ και τιμή τον χαρακτήρα
fm.close()
print(morse)
input_file=input('Δώσε αρχείο morse >')     # Δοκιμάστε το morse_in.txt
fin=open(input_file,'r',encoding='ascii')
fout=open('text_out.txt','w')
for frasi in fin:
    lexeis=frasi.split(7*' ')           # Διαχωρίζει τη φράση όταν βρει 7 κενά. Κάθε στοιχειο της λίστας περιέχει μια λέξη
    for lex in lexeis:                      # Στη μεταβλητή lex ανατιθενται οι κωδικοί κάθε λέξης
        lex_list=lex.split()                # Στη λίστα lex_list καταχωρούνται οι διαφορετικές λέξεις
        for m in lex_list:                  # Στη μεταβλητή m ανατίθενται οι κωδικοί κάθε χαρακτήρα
            ch=morse.get(m)                 # Στο λεξικό εντοπίζεται ο χαρακτηρας του κωδικού
            fout.write(ch)
        fout.write(' ')
print('\n########### ΤΕΛΟΣ ###########')
fin.close()
fout.close()
