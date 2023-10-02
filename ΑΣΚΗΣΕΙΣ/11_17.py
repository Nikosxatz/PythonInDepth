fm=open('morse.txt','r',encoding='cp1253')
morse=dict()
for m in fm:
    line=m.split()
    morse.update({line[0]:line[1]})             # Καταχώριση των κωδικών Μορς στο λεξικό morse με κλειδί τον χαρακτήρα
fm.close()
input_file=input('Δώσε αρχείο για μετατροπή >')
fin=open(input_file,'r',encoding='ascii')
fout=open('morse_out.txt','w')
for frasi in fin:
    frasi=frasi.upper()                         
    lexeis=frasi.split()                        # Στη λίστα lexeis καταχωρίζονται οι λέξεις της φράσης
    # print(lexeis)
    for lex in lexeis:
        for ch in lex:                          # Στη μεταβλητή ch ανατίθενται ένα προς ένα τα γράμματα της λέξης
            code=morse.get(ch)                  # Εντοπίζει στο λεξικό την ακολουθία Μορς του χαρακτηρα ch                  
            fout.write(code)
            fout.write(3*' ')                   # Εγγράφει 3 κενά μετά από κάθε γράμμα
        fout.write(7*' ')                       # Εγγράφει 7 κενά μετά από κάθε λέξη
print('\n########### ΤΕΛΟΣ ###########')
fin.close()
fout.close()
