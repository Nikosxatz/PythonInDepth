try:
  a=float(input('Δώσε αριθμό :'))
  b=float(input('Δώσε και άλλον αριθμό :'))
  if b<0.01 and b>0:
    raise ZeroDivisionError('Πολυ μικρός ... κοντα στο 0!')
  else:
    print(a/b)
except ValueError as e1:
  print('Πρόσεξε τι πληκτρολογείς!')  
  print(e1)  
except ZeroDivisionError as e2:
  print(e2)
except:
  print('Κάτι πήγε στραβά!!!')
