try:
  a=int(input('Δώσε αριθμό :'))
  b=int(input('Δώσε και άλλον αριθμό :'))
  print(a/b)
  if a>b:
    c=a
  print(c)
except NameError as e1:
  print('Εππ... κατι ξέχασες!')  
  print(e1)  
except (ZeroDivisionError,ValueError) as e2:
  print('Πρόσεξε τι πληκτρολογείς!',e2)
except:
  print('Κάτι πήγε στραβά!!!')
