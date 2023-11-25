try:
  epilogi=int(input('Δώσε αριθμό:'))
  if epilogi==1:
    raise ValueError(5)
  elif epilogi==2:
    raise ValueError('Πρόβλημα')
  elif epilogi==3:
    a=10
    b=20
    raise ValueError(a,b,'Τέλος')
  else:
    raise ValueError('Κάτι άλλο πάτησες')
except ValueError as e1:
  print('Τιμή του αντικειμένου εξαίρεσης:',e1)
  print(e1.__str__())
  print(str(e1))
  if str(e1)=='5':
    print('Πάτησες 1')
  elif str(e1)=='Πρόβλημα':
    print('Πάτησες 2')
    



