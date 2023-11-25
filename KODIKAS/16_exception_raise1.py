try:
  a=float(input('Δώσε αριθμό :'))
  b=float(input('Δώσε και άλλον αριθμό :'))
  c=a/b
  if b<0.01 and b>0:
    raise ZeroDivisionError
  print(c)
except ZeroDivisionError as e1:
  print('Πρόβλημα στη διαίρεση ',e1)
except:
  print('Κάτι άλλο πήγε στραβά:')

