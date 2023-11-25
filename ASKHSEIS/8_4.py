def dieretes(ar):
    t=()
    for i in range(2,ar//2+1):
        if ar%i==0:
            t=t+(i,)
    return t

# Κυρίως πρόγραμμα
num=int(input('Δώσε έναν ακέραιο αριθμό:'))
print('Οι γνήσιοι διαιρέτες του',num,'είναι =',dieretes(num))


        
