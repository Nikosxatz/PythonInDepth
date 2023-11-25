def rev(num):
    sum=0
    while True:
        digit=num%10
        sum=(sum*10)+digit
        num=num//10
        if num==0: break
    return sum


# Κυρίως πρόγραμμα
ar=int(input('Δώσε αριθμό:'))
print('Ο κατοπτρικός του',ar,'είναι:',rev(ar))

