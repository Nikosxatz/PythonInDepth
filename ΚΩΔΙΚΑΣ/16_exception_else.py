try:
  a=int(input('Δώσε αριθμό :'))
  b=int(input('Δώσε και άλλον αριθμό :'))
  c=a/b
except ZeroDivisionError:
  print('Πρόσεξε τι πληκτρολογείς!')
except:
  print('Κάτι άλλο πήγε στραβά!!!')
else:
  print('Αποτέλεσμα =',c)
finally:
  print('=== ΤΕΛΟΣ ===')


