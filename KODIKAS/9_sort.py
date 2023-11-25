import random

def bubblesort(Lst):
    n=len(Lst)
    for i in range(n):
        for k in range(n-1,i,-1):
            if Lst[k]<Lst[k-1]:
                temp=Lst[k]
                Lst[k]=Lst[k-1]
                Lst[k-1]=temp
      
def bubblesort2(Lst):
    n=len(Lst)
    for i in range(n):
        found=False
        for k in range(n-1,i,-1):
            if Lst[k]<Lst[k-1]:
                temp=Lst[k]
                Lst[k]=Lst[k-1]
                Lst[k-1]=temp
                found=True
        if not found: break

def selectsort(Lst):
    n=len(Lst)
    for i in range(n-1,0,-1):
        max=Lst[0]
        maxpos=0
        for k in range(i+1):
            if Lst[k]>max:
                max=Lst[k]
                maxpos=k
        Lst[i],Lst[maxpos]=Lst[maxpos],Lst[i]
  
def q_sort(Lst,apo,eos):
    if eos<=apo:
        return
    diax_timi=Lst[apo]
    min=apo
    max=eos
    while min<max:
        while Lst[min]<=diax_timi:
            min=min+1
            if min>=max: break
        while Lst[max]>diax_timi:
            max=max-1
        if min<max:
            temp=Lst[min]
            Lst[min]=Lst[max]
            Lst[max]=temp
    Lst[apo]=Lst[max]
    Lst[max]=diax_timi
    diax_pos=max
    q_sort(Lst,apo,diax_pos-1)
    q_sort(Lst,diax_pos+1,eos)
    
a=[7,23,4,6,78,3,34,56,21,12]
bubblesort(a)
print(a)
a=[7,23,4,6,78,3,34,56,21,12]
bubblesort2(a)
print(a)
a=[7,23,4,6,78,3,34,56,21,12]
selectsort(a)
print(a)
a=[7,23,4,6,78,3,34,56,21,12]
q_sort(a,0,9)
print(a)
