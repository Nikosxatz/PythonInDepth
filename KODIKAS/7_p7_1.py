def To_celsium(f):
    return (f-32)*5/9

# Κυρίως πρόγραμμα
sum=0
for i in range(1,25):
    print('Θερμοκρασία ώρας ',i,' σε βαθμούς Fahrenheit: ',end='')
    ft=float(input())
    ct=To_celsium(ft)
    sum=sum+ct
mo=sum/24
print('Η μέση θερμοκρασία ημέρας είναι ',mo)

 
