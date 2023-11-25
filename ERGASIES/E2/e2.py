def disekto(e):
    if (e%4==0 and e%100!=0) or e%400==0:
        return True
    else:
        return False

def imera(h,m,e):
    a=365*(e-1)
    b1=(e-1)//4
    b2=-((e-1)//100)
    b3=(e-1)//400
    g=(367*m-362)//12
    if m<=2:
        d=0
    elif m>2 and disekto(e):
        d=-1
    else:
        d=-2
    s=a+b1+b2+b3+g+h+d
    x=s%7
    return x

def emfanisi_imeras(h,m,e):
    ar_im=imera(h,m,e)
    meres=('Κυριακή','Δευτέρα','Τρίτη','Τετάρτη','Πέμπτη','Παρασκευή','Σαββάτο')	
    print('Η ημέρα στις {}/{}/{} είναι'.format(h,m,e),meres[ar_im])

# Κυρίως πρόγραμμα
etos=int(input('Δώσε έτος:'))
emfanisi_imeras(1,1,etos);
emfanisi_imeras(6,1,etos);
emfanisi_imeras(25,3,etos);
emfanisi_imeras(15,8,etos);
emfanisi_imeras(28,10,etos);
emfanisi_imeras(25,12,etos);
emfanisi_imeras(26,12,etos);
