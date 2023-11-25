import random
number=random.randint(1,1000)
while True:
    num = int(input('Δώσε ακέραιο αριθμό από 1~1000 > '))
    if num < number:
        print('Ο κρυφός αριθμός είναι πιο μεγάλος')           
    elif num > number:
        print('Ο κρυφός αριθμός είναι πιο μικρός')  
    else:
        break
print('Μπράβο τον βρήκες!!!')
