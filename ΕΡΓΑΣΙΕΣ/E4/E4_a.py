def monades(ar,pl):
    mon_en=('','Ένα ','Δύο ','Τρία ','Τέσσερα ','Πέντε ','Έξι ','Επτά ','Οκτώ ','Ενιά ','Δέκα ','Έντεκα ','Δώδεκα ')
    mon_pl=('','Μία ','Δύο ','Τρεις ','Τέσσερις ','Πέντε ','Έξι ','Επτά ','Οκτώ ','Ενιά ','Δέκα ','Έντεκα ','Δώδεκα ')
    if pl:
        return mon_pl[ar]
    else:
        return mon_en[ar]

def dekades(ar):
    dk=('','Δέκα ','Είκοσι ','Τριάντα ','Σαράντα ','Πενήντα ','Εξήντα ','Εβδομήντα ','Ογδόντα ','Ενενήντα ')
    return dk[ar]
   
def ekatontades(ar,pl):
    ek_en=('','Εκατό ','Διακόσια ','Τριακόσια ','Τετρακόσια ','Πεντακόσια ','Εξακόσια ','Επτακόσια ','Οκτακόσια ','Ενιακόσια ')
    ek_pl=('','Εκατό ','Διακόσιες ','Τριακόσιες ','Τετρακόσιες ','Πεντακόσιες ','Εξακόσιες ','Επτακόσιες ','Οκτακόσιες ','Ενιακόσιες ')
    if pl: 
        return ek_pl[ar]
    else:
        return ek_en[ar]

def tripsifio(ar,pl):
    e=ar//100
    d=(ar%100)//10
    m=ar%10
    mm=ar%100
    lex=''
    if e!=0:
        lex=lex+ekatontades(e,pl)
    if mm>12:
        if d!=0:
            lex=lex+dekades(d)
        if m!=0:
            lex=lex+monades(m,pl)
    elif mm!=0:
        lex=lex+monades(mm,pl)   
    return lex

# Κυρίως πρόγραμμα
olo=''
a=int(input('Δώσε έναν αριθμό:'))
if a<0: 
    olo+='Μείον '
    a=-a
ek=a//1000000
xl=(a%1000000)//1000
yp=a%1000
if ek>0:
    olo+=tripsifio(ek,False)
    if ek==1:
        olo+='εκατομμύριο '		
    else:
        olo+='εκατομμύρια '    
if xl>0: 
    if xl==1:
        olo+='χίλια ' 
    else:
        olo+=tripsifio(xl,True)
        olo+='χιλιάδες ' 
if yp>0: 
    olo+=tripsifio(yp,False)
if a==0: 
    print('Μηδέν')
else:  
    print(olo)
  
   
