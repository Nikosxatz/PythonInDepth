try:
  a=float(input('Δώσε αριθμό :'))
  b=float(input('Δώσε και άλλον αριθμό :'))
  print(a/b)
  power=a**b
  if a>b:
    c=a
  print(c)
except ArithmeticError as e1:
  print('Κάποιες πράξεις δεν γίνονται ...',e1)  
except Exception as e2:
  print('Κάτι άλλο πήγε στραβά:',e2)

