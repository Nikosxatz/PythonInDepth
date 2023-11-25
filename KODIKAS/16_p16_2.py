import random
class LathosArithmos(Exception):
    pass

class PoliMikros(LathosArithmos):
    def __init__(self,ar):
        self.timi=ar
    def __str__(self):
        return 'O αριθμός '+str(self.timi)+' είναι πολύ μικρός'

class PoliMegalos(LathosArithmos):
    def __init__(self,ar):
        self.timi=ar   
    def __str__(self):
        return 'O αριθμός '+str(self.timi)+' είναι πολύ μεγάλος'

number=random.randint(1,1000)
while True:
    try:
        num = int(input('Δώσε ακέραιο αριθμό από 1~1000 > '))
        if num < number:
            raise PoliMikros(num)            
        elif num > number:
            raise PoliMegalos(num)
        break
    except PoliMikros as e1:
        print(e1)
    except PoliMegalos as e2:
        print(e2)
    else:
        break
    finally:
        print('----------------------')

print('Μπράβο τον βρήκες!!!')
