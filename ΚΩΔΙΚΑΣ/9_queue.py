def eisagogi(Lst,o):
    Lst.append(o)
      
def exagogi(Lst):
    n=len(Lst)    
    if n==0:
        print('Η ουρά είναι άδεια!')
        return
    s=Lst.pop(0)
    print('Το στοιχείο',s,'απομακρύνθηκε')

def emfanisi(Lst):
    print('Αρχη ουράς -> ',end='')
    print(Lst, end='')
    print(' <- Τέλος ουράς')

def main():
    queue=list()
    while True:
        e=int(input('0->Εξοδος 1->Εισαγωγή 2->Εξαγωγή 3->Εμφάνιση : '))
        if e==0:
            break
        elif e==1:
            item=input('Δώσε τιμή :')
            eisagogi(queue,item)
        elif e==2:
            exagogi(queue)    
        elif e==3:
            emfanisi(queue)

#Κυρίως πρόγραμμα
main()
