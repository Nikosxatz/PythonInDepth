def reverse(ar):
    if ar==0:
        return
    else:
        print(ar%10,end='')
        return reverse(ar//10)

# Κυρίως πρόγραμμα
x=int(input('Δώσε έναν αριθμό:'))
reverse(x)






















