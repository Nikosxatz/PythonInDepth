def othisi(Lst,o):
    Lst.append(o)
      
def apothisi(Lst):
    n=len(Lst)    
    if n==0:
        print('Η στοιβα είναι άδεια!')
        return
    s=Lst.pop(n-1)
    print('Το στοιχείο',s,'απομακρύνθηκε')

def emfanisi(Lst):
    n=len(Lst)
    for i in range(n-1,-1,-1):
        print(Lst[i])

def main():
    stack=list()
    while True:
        e=int(input('0->Εξοδος 1->Ωθηση 2->Απώθηση 3->Εμφάνιση : '))
        if e==0:
            break
        elif e==1:
            item=input('Δώσε τιμή :')
            othisi(stack,item)
        elif e==2:
            apothisi(stack)    
        elif e==3:
            emfanisi(stack)

# Κυρίως πρόγραμμα
main()
