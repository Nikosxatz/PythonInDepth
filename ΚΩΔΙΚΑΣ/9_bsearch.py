import random

def binary(Lst,timi):
    apo=0
    eos=len(Lst)-1
    while apo<=eos:
        meson=(apo+eos)//2
        if timi<Lst[meson]:
            eos=meson-1
        elif timi>Lst[meson]:
            apo=meson+1
        else:
            return meson
    return -1

def rbinary(Lst,apo,eos,timi):
    if apo<=eos:
        meson=(apo+eos)//2
        if timi<Lst[meson]:
            return rbinary(Lst,apo,meson-1,timi)
        elif timi>Lst[meson]:
            return rbinary(Lst,meson+1,eos,timi)
        else:
            return meson
    else:
        return -1

    
a=[7,12,29,48,69,100,135,180,196,205]
print('Στοιχεία λίστας=',a)
print('#### Αναζήτηση με χρήση της συνάρτησης binary() ####')
timi=int(input('Δωσε τιμή για αναζήτηση:'))
thesi=binary(a,timi)
if thesi!=-1:
    print('Η τιμή βρέθηκε στη θέση',thesi)
else:
    print('Η τιμή δεν βρέθηκε στη λίστα')

print('#### Αναζήτηση με χρήση της αναδρομικής συνάρτησης rbinary() ####')
timi=int(input('Δωσε τιμή για αναζήτηση:'))
thesi=rbinary(a,0,9,timi)
if thesi!=-1:
    print('Η τιμή βρέθηκε στη θέση',thesi)
else:
    print('Η τιμή δεν βρέθηκε στη λίστα')
